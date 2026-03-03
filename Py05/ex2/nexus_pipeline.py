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
            result = defaultdict(lambda: None, {key: None for key in data.split(",")})
        return result


class TransformStage:
    def __init__(self) -> None:
        pass

    def validate_stream(self, data: dict) -> bool:
        for data in data.items():
            if "temp" not in data[0] or not isinstance(data[1], float):
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
        if data["adapter"] == "json":
            temp = data['value']
            result = f"Output: Processed temperature reading: {temp}°{data['unit']} {'(Normal range)' if isinstance(temp, float) and temp < 32 and temp > 12 else ''}"
        elif data["adapter"] == "cvs":
            result = "Output: User activity logged: "
        elif data["adapter"] == "stream":
            result = "Output: Stream summary: "
        else:
            raise ErrorStage(f"Error Outpustage: adapter unknown: {data.get('adapter')}")
        return result


class ProcessingPipeline(ABC):
    def __init__(self):
        self.stages: list[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage):
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self):
        super().__init__()

    def process(self, data: Any) -> Union[str, Any]:
        for stage in self.stages:
            data = stage.process(data)
        return data


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
    str_test = jtest.process(data_test)
    print(str_test)