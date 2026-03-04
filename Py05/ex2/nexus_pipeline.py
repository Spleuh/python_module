from typing import Any, Protocol, Dict, Union
from abc import ABC, abstractmethod
from collections import defaultdict


class ErrorJSON(Exception):
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
            if data["adapter"] == "json":
                result = self.format_json(data)
            elif data["adapter"] == "cvs":
                result = "Output: User activity logged: "
            elif data["adapter"] == "stream":
                result = "Output: Stream summary: "
            else:
                raise ErrorStage("Error Outpustage: adapter unknown: "
                                 f"{data.get('adapter')}")
        else:
            raise ErrorStage(f"Error Stage 2, data not transformed: {data}")
        return result

    def format_json(self, data: Any) -> str:
        temp = data['value']
        unit = data['unit']
        if not isinstance(temp, float):
            raise ErrorStage(f"Error type: temp {temp}")
        if 12 < temp < 32:
            range = "(Normal range)"
        else:
            range = ""
        if unit not in ["K", "C", "F"]:
            raise ErrorStage(f"Error type: unit {unit}")
        result = ("Output: Processed temperature reading: "
                  f"{temp}°{unit} {range}")
        return result


class ProcessingPipeline(ABC):
    def __init__(self):
        self.stages: list[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage):
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)


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

    def validate(self, tmp: list[list[str]]) -> bool:
        for i in tmp:
            for j in i:
                if not isinstance(j[0], str):
                    return False
        return True

    def pre_process(self, data: Any):
        result: dict[str: str | float] = {}
        if isinstance(data, str):
            tmp = data.split(",")
            tmp = [splited for t in tmp for splited in [t.split(":")]]
            if not self.validate(tmp):
                raise ErrorJSON("Data not formated, type value != str "
                                f"or float {tmp}")
            result = {str(kv[0]): str(kv[1]) for kv in tmp}
            print(type(result))
            print(result)

    def post_process(self, data: Any):
        pass

    def process(self, data: Any) -> Union[str, Any]:
        data = self.pre_process(data)
        result = super().process(data)
        result = self.post_process(result)
        return result


class CSVStream(ProcessingPipeline):
    def __init__(self):
        super().__init__()

    def process(self, data: Any) -> Union[str, Any]:
        for stage in self.stages:
            data = stage.process(data)
        return data


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
    jtest = JSONAdapter()
    jtest.add_stage(InputStage())
    jtest.add_stage(TransformStage())
    jtest.add_stage(OutputStage())
    data_test = {"sensor": "temp", "value": 23.5, "unit": "C"}
    str_test = "sensor:temp,value:23.5,unit:C"
    str_test = jtest.process(str_test)
    print(str_test)