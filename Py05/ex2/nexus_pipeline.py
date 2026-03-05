from typing import Any, Protocol, Dict, Union
from abc import ABC, abstractmethod
from collections import defaultdict


class ErrorChaining(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class ErrorJSON(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class ErrorCSV(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class ErrorStream(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class ErrorStage(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage:
    def __init__(self) -> None:
        pass

    def process(self, data: Any) -> Dict:
        if isinstance(data, dict):
            result = defaultdict(lambda: None, data)
        else:
            result = defaultdict(lambda: None,
                                 {key: None for key in data.split(",")})
        return result


class TransformStage:
    def __init__(self) -> None:
        pass

    def validate_stream(self, data: dict) -> bool:
        for d in data.items():
            if "temp" not in d[0] or not isinstance(d[1], float):
                return False
        return True

    def process(self, data: Any) -> Dict:
        if data['adapter'] is not None:
            data["transformed"] = True
        return data


class OutputStage:
    def __init__(self) -> None:
        pass

    def process(self, data: Any) -> str:
        result = ""
        if data['transformed']:
            result = "Output: "
        else:
            raise ErrorStage(f"Error Stage 2, data not transfomed: {data}")
        return result


class ProcessingPipeline(ABC):
    def __init__(self, id: str):
        self.stages: list[ProcessingStage] = []
        self.id = id

    def add_stage(self, stage: ProcessingStage):
        self.stages.append(stage)

    def stage_process(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)
        return data

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


def convert(value: Any) -> str | int | float:
    try:
        return (float(value))
    except ValueError:
        try:
            return (int(value))
        except ValueError:
            try:
                return (str(value))
            except Exception as e:
                print(f"{e}")


class JSONAdapter(ProcessingPipeline):
    def __init__(self, id: str):
        super().__init__(id)

    def validate(self, data: dict[str, str]) -> bool:
        for i in data.items():
            tmp = convert(i[1])
            if convert(i[0]) == "value":
                if not isinstance(tmp, float):
                    return False
            elif not isinstance(i[0], str) or not isinstance(tmp, (str)):
                return False
        return True

    def pre_process(self, data: Any) -> Any:
        if isinstance(data, str):
            tmp = data.split(",")
            tmp = [splited for t in tmp for splited in [t.split(":")]]
            result = {str(kv[0]): str(kv[1]) for kv in tmp}
        elif isinstance(data, list):
            tmp = data
            result = {str(kv[0]): str(kv[1]) for kv in tmp}
        elif isinstance(data, dict):
            result = data
        else:
            raise ErrorJSON(f"Error format data not supported: {data}")
        if not self.validate(result):
            raise ErrorJSON("Data not formated, type value != str "
                            f"or float {result}")
        return result

    def post_process(self, data: Any) -> str:
        temp = data['value']
        unit = data['unit']
        temp = convert(temp)
        if not isinstance(temp, float):
            raise ErrorStage(f"Error type: temp {temp}")
        if 12 < temp < 32:
            range = "(Normal range)"
        else:
            range = ""
        if unit not in ["K", "C", "F"]:
            raise ErrorStage(f"Error type: unit {unit}")
        result = ("Processed temperature reading: "
                  f"{temp}°{unit} {range}")
        return result

    def process(self, data: Any) -> Union[str, Any]:
        data = self.pre_process(data)
        data['adapter'] = 'json'
        result = super().stage_process(data)
        result = result + self.post_process(data)
        return result


class CSVAdapter(ProcessingPipeline):
    def __init__(self, id: str):
        super().__init__(id)

    def validate(self, data: dict) -> bool:
        keys = ["user", "action", "timestamp"]
        for i in data.items():
            if i[0] not in keys or not isinstance(i[1], int):
                return False
        return True

    def pre_process(self, data: Any) -> Dict:
        if isinstance(data, str):
            tmp = data.split(",")
        elif isinstance(data, list):
            tmp = data
        else:
            raise ErrorCSV(f"Error format data not supported: {data}")
        result = {"user": 0, "action": 0, "timestamp": 0}
        result = {key: value + 1 for key, value in result.items()
                  for t in tmp if t == key}
        if not self.validate(result):
            raise ErrorCSV("Data not formated, keyword unknown "
                           f"(user, action, timestamp): {result}")
        return result

    def post_process(self, data: Any) -> Any:
        result = f"User activity logged: {data['action']} actions processed"
        return result

    def process(self, data: Any) -> Union[str, Any]:
        data = self.pre_process(data)
        data['adapter'] = 'csv'
        result = super().stage_process(data)
        result = result + self.post_process(data)
        return result


class StreamAdapter(ProcessingPipeline):
    def __init__(self, id: str):
        super().__init__(id)

    def validate(self, data: dict) -> bool:
        for key, value in data.items():
            if not isinstance(key, str) or \
                    not isinstance(value, (float, int)):
                return False
            elif key not in ["sum_temp", "count"]:
                return False
        return True

    def pre_process(self, data: Any) -> Dict:
        if isinstance(data, str):
            tmp = data.split(",")
            tmp = [t.split(":") for t in tmp]
        elif isinstance(data, list):
            tmp = data
        else:
            raise ErrorStream("ErrorStream: data type input not"
                              f" supported: {data}")
        result = {"sum_temp": 0, "count": 0}
        for t in tmp:
            if t[0] == "temp":
                result['sum_temp'] += convert(t[1])
                result['count'] += 1
        if not self.validate(result):
            raise ErrorStream(f"ErrorStream invalide key or value: {result}")
        return result

    def post_process(self, data: Any) -> str:
        result = (f"Stream summary: {data['count']} readings, avg: "
                  f"{(data['sum_temp'] / data['count']):.1f}°C")
        return result

    def process(self, data: Any) -> Union[str, Any]:
        data = self.pre_process(data)
        data.update({'adapter': 'stream'})
        result = super().stage_process(data)
        result = result + self.post_process(data)
        return result


class Pipeline_A(ProcessingPipeline):
    def __init__(self, id: str):
        super().__init__(id)

    def process(self, data):
        if not isinstance(data, str):
            raise ErrorChaining(f"ErrorChaining data type: {data}")
        result = data.split(",")
        result = [s.split(":") for s in result]
        return result


class Pipeline_B(ProcessingPipeline):
    def __init__(self, id: str):
        super().__init__(id)

    def init_dict(self, data: list) -> dict:
        result = defaultdict(int)
        count = 0
        for i in data:
            key, value = i
            if key != 'temp':
                result[key] = value
            else:
                count += 1
                result[key] = result[key] + convert(value)
        result['count'] = count
        return result

    def verif(self, data: list) -> bool:
        for i in data:
            key, value = i
            if key == "temp" and not isinstance(convert(value), float):
                return False
        return True

    def process(self, data):
        if not isinstance(data, list):
            raise ErrorChaining(f"ErrorChaining input: {data}")
        if not self.verif(data):
            raise ErrorChaining("ErrorChaining error stage 2 "
                                f"data type: {data}")
        result = self.init_dict(data)
        return result


class Pipeline_C(ProcessingPipeline):
    def __init__(self, id: str):
        super().__init__(id)

    def process(self, data):
        avg = data['temp'] / data['count']
        data['avg'] = f"{avg:.2f}"
        return dict(data)


class NexusManager:
    def __init__(self):
        self.adapters: list[ProcessingPipeline] = []
        self.chaining: list[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        if "adapter" in pipeline.id:
            self.adapters.append(pipeline)
        elif "chaining" in pipeline.id:
            self.chaining.append(pipeline)

    def process_data(self, data: Any, id: str) -> str | None:
        result = data
        if "adapter" in id:
            for pipeline in self.adapters:
                if id == pipeline.id:
                    result = pipeline.process(result)
        elif "chaining" in id:
            self.chaining.sort(key=lambda p: p.id)
            for pipeline in self.chaining:
                result = pipeline.process(result)
        return result


def demo_adapter():
    try:
        print('=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n')
        print('Initializing Nexus Manager...')
        nexus = NexusManager()
        print('Pipeline capacity: 1000 streams/second\n')
        jtest = JSONAdapter("adapter:json")
        jtest.add_stage(InputStage())
        jtest.add_stage(TransformStage())
        jtest.add_stage(OutputStage())
        csvtset = CSVAdapter("adapter:csv")
        csvtset.add_stage(InputStage())
        csvtset.add_stage(TransformStage())
        csvtset.add_stage(OutputStage())
        streamtest = StreamAdapter("adapter:stream")
        streamtest.add_stage(InputStage())
        streamtest.add_stage(TransformStage())
        streamtest.add_stage(OutputStage())
        nexus.add_pipeline(jtest)
        nexus.add_pipeline(csvtset)
        nexus.add_pipeline(streamtest)

        print('Creating Data Processing Pipeline...')
        print('Stage 1: Input validation and parsing')
        print('Stage 2: Data transformation and enrichment')
        print('Stage 3: Output formatting and delivery\n')
        print('=== Multi-Format Data Processing ===\n')
        print('Processing JSON data through pipeline...')
        data_test = {"sensor": "temp", "value": 23.5, "unit": "C"}
        print(f'Input: {data_test}')
        print('Transform: Enriched with metadata and validation')
        str_test = "sensor:temp,value:23.5,unit:C"
        str_test = nexus.process_data(data_test, "adapter:json")
        print(str_test)

        print('\nProcessing CSV data through same pipeline...')
        csv_data = "user,action,timestamp"
        print(f'Input: {csv_data}')
        print('Transform: Parsed and structured data')
        result_csv = nexus.process_data(csv_data, "adapter:csv")
        print(result_csv)

        print('\nProcessing Stream data through same pipeline...')
        print('Input: Real-time sensor stream')
        print('Transform: Aggregated and filtered')
        stream_data = ("temp:21.8,temp:22.3,temp:22.0,temp:22.5,temp:21.9")
        result_stream = nexus.process_data(stream_data, "adapter:stream")
        print(result_stream)

        print('\n=== Pipeline Chaining Demo ===')
    except Exception as e:
        print(f"{e}")


def demo_chaining():
    try:
        nexus = NexusManager()
        p_a = Pipeline_A("chaining:a")
        p_b = Pipeline_B("chaining:b")
        p_c = Pipeline_C("chaining:c")
        nexus.add_pipeline(p_a)
        nexus.add_pipeline(p_b)
        nexus.add_pipeline(p_c)
        raw_data = ("time:05-03-2026,unit:C,temp:21.8,"
                    "temp:22.3,temp:22.0,temp:22.5,temp:21.9")
        test = nexus.process_data(raw_data, "chaining")
        print(test)
    except Exception as e:
        print({e})


if __name__ == "__main__":
    demo_adapter()
    demo_chaining()
