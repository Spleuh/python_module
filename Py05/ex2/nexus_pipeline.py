from typing import Collection, Any, Protocol, Dict, Union
from abc import ABC, abstractmethod


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage:
    def __init__(self) -> None:
        pass

    def process(self, data: Any) -> Dict:
        return data


class TransformStage:
    def __init__(self) -> None:
        pass

    def process(self, data: Any) -> Dict:
        return data


class OutputStage:
    def __init__(self) -> None:
        pass

    def process(self, data: Any) -> str:
        return data

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


class CVSAdapter(ProcessingPipeline):
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
    pass
