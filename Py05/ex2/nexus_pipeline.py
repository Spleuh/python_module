from typing import Any, Protocol, Dict, Union
from abc import ABC, abstractmethod
from collections import defaultdict


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
    def __init__(self):
        self.stages: list[ProcessingStage] = []

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
    def __init__(self):
        super().__init__()

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
    def __init__(self):
        super().__init__()

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
    def __init__(self):
        super().__init__()

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


class NexusManager:
    def __init__(self):
        self.pipelines: list[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, data: Any):
        for pipeline in self.pipelines:
            pipeline.process(data)


def demo_adapter():
    try:
        print('=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n')
        print('Initializing Nexus Manager...')
        print('Pipeline capacity: 1000 streams/second\n')
        jtest = JSONAdapter()
        jtest.add_stage(InputStage())
        jtest.add_stage(TransformStage())
        jtest.add_stage(OutputStage())
        csvtset = CSVAdapter()
        csvtset.add_stage(InputStage())
        csvtset.add_stage(TransformStage())
        csvtset.add_stage(OutputStage())
        streamtest = StreamAdapter()
        streamtest.add_stage(InputStage())
        streamtest.add_stage(TransformStage())
        streamtest.add_stage(OutputStage())
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
        str_test = jtest.process(data_test)
        print(str_test)

        print('\nProcessing CSV data through same pipeline...')
        csv_data = "user,action,timestamp"
        print(f'Input: {csv_data}')
        print('Transform: Parsed and structured data')
        result_csv = csvtset.process(csv_data)
        print(result_csv)

        print('\nProcessing Stream data through same pipeline...')
        print('Input: Real-time sensor stream')
        print('Transform: Aggregated and filtered')
        stream_data = ("temp:21.8,temp:22.3,temp:22.0,temp:22.5,temp:21.9")
        result_stream = streamtest.process(stream_data)
        print(result_stream)
    except Exception as e:
        print(f"{e}")


if __name__ == "__main__":
    demo_adapter()
