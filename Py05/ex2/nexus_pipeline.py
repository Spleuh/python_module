from typing import Any, Protocol, Dict, Union
from abc import ABC, abstractmethod
from collections import defaultdict


class ErrorJSON(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class ErrorCVS(Exception):
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

    def add_adapter(self, data: Any) -> Dict:
        json_keys = {"sensor", "value", "unit"}
        csv_keys = {"user", "action", "timestamp"}
        data_keys = set(data.keys())
        if len(json_keys.difference(data_keys)) == 0:
            data["adapter"] = "json"
        elif len(csv_keys.difference(data_keys)) == 0:
            data["adapter"] = "csv"
        elif self.validate_stream(data):
            data["adapter"] = "stream"
        else:
            raise ErrorStage("type data unknown")
        return data

    def process(self, data: Any) -> Dict:
        data = self.add_adapter(data)
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
        return (int(value))
    except ValueError:
        try:
            return (float(value))
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
        result = super().stage_process(data)
        result = result + self.post_process(data)
        return result


class CSVStream(ProcessingPipeline):
    def __init__(self):
        super().__init__()

    def validate(self, data: str) -> bool:
        tmp = data.split(",")
        for i in tmp:
            if i not in ["user", "action", "timestamp"]:
                return False
        return True

    def pre_process(self, data: Any) -> Any:
        if isinstance(data, str):
            result = data
        elif isinstance(data, list):
            result = ",".join(data)
        else:
            raise ErrorCVS(f"Error format data not supported: {data}")
        if not self.validate(result):
            raise ErrorCVS("Data not formated, keyword unknown "
                           f"(user, action, timestamp): {result}")
        return result

    def post_process(self, data: Any) -> Any:
        data = data.split(",")
        action = len([count for count in data if count == "action"])
        result = f"User activity logged: {action} actions processed"
        return result

    def process(self, data: Any) -> Union[str, Any]:
        data = self.pre_process(data)
        result = super().stage_process(data)
        result = result + self.post_process(data)
        return result


class StreamAdapter(ProcessingPipeline):
    def __init__(self):
        super().__init__()

    def process(self, data: Any) -> Union[str, Any]:
        for stage in self.stages:
            data = stage.process(data)
        return data


class NexusManager:
    def __init__(self):
        self.pipelines: list[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, data: Any):
        for pipeline in self.pipelines:
            pipeline.process(data)


if __name__ == "__main__":
    try:
        jtest = JSONAdapter()
        jtest.add_stage(InputStage())
        jtest.add_stage(TransformStage())
        jtest.add_stage(OutputStage())
        csvtset = CSVStream()
        csvtset.add_stage(InputStage())
        csvtset.add_stage(TransformStage())
        csvtset.add_stage(OutputStage())
        streamtest = StreamAdapter()
        streamtest.add_stage(InputStage())
        streamtest.add_stage(TransformStage())
        streamtest.add_stage(OutputStage())

        data_test = {"sensor": "temp", "value": 23.5, "unit": "C"}
        str_test = "sensor:temp,value:23.5,unit:C"
        str_test = jtest.process(str_test)
        print(str_test)

        csv_data = "user,action,timestamp"
        result_csv = csvtset.process(csv_data)
        print(result_csv)

        stream_data = 
    except Exception as e:
        print(f"{e}")
