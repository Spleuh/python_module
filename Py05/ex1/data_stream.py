from typing import Any, List, Dict, Optional, Union
from abc import ABC, abstractmethod


def convert(value: Any) -> int | float | str | None:
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            try:
                str(value)
            except ValueError:
                pass
    return None


class DataStream(ABC):
    def __init__(self, stream_id: str, types: List[str]):
        self.id = stream_id
        type_criterias = types.split(':')
        self.type = type_criterias[0]
        self.lst_crit = type_criterias[1:]

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return ([data.split(":", 1)[1] for data in data_batch if
                     isinstance(data, str) and
                     len([crit for crit in self.lst_crit if
                          crit in data and self.id in data]) > 0])
        else:
            return ([data.split(":", 1)[1] for data in data_batch if
                     isinstance(data, str) and criteria in data and
                     self.id in data])

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id: str, types: str):
        super().__init__(stream_id, types)

    def process_batch(self, data_batch) -> str:
        self.data = self.filter_data(data_batch)
        return ", ".join(self.data)

    def get_stats(self) -> Dict[str, float]:
        stats = {}
        for t in self.lst_crit:
            values = ([convert(key_value[1]) for data in self.data for
                       key_value in [data.split(":")]
                       if len(key_value) == 2 and key_value[0] == t])
            total = sum(values)
            count = len(values)
            if count != 0:
                stats.update({t: total/count})
        return stats


class TransactionStream(DataStream):
    def __init__(self, stream_id, types):
        super().__init__(stream_id, types)

    def process_batch(self, data_batch) -> str:
        self.data = self.filter_data(data_batch)
        return ", ".join(self.data)

    def get_stats(self) -> Dict[str, int]:
        stats = {"net_flow": 0}
        values = []
        for t in self.lst_crit:
            if t == "buy":
                i = 1
            elif t == "sell":
                i = -1
            values += ([convert(key_value[1]) * i for data in self.data for
                       key_value in [data.split(":")]
                       if len(key_value) == 2 and key_value[0] == t])
        stats["net_flow"] = sum(values)
        return stats


class EventStream(DataStream):
    def __init__(self, stream_id, types):
        super().__init__(stream_id, types)

    def process_batch(self, data_batch):
        self.data = self.filter_data(data_batch)
        return ", ".join(self.data)

    def get_stats(self) -> Dict[str, int]:
        stats = {key: self.data.count(key) for key in self.data}
        return stats


class StreamProcessor():
    def __init__(self, streams: List[DataStream]):
        self.streams = streams

    def process(self,  data_batch: List[Any]):
        for stream in self.streams:
            stream.process_batch(data_batch)


if __name__ == "__main__":
    data_batch = [
        # SensorStream
        "SENSOR_001:temp:22.5",
        "SENSOR_001:humidity:65",
        "SENSOR_001:pressure:1013",
        "SENSOR_002:temp:23.1",
        "SENSOR_002:humidity:60",

        # TransactionStream
        "TRANS_001:buy:100",
        "TRANS_001:sell:150",
        "TRANS_001:buy:75",
        "TRANS_002:buy:200",
        "TRANS_002:sell:50",

        # EventStream
        "EVENT_001:login",
        "EVENT_001:error",
        "EVENT_001:logout",
        "EVENT_002:shutdown",
        "EVENT_002:restart"
    ]

    print('=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n')

    print("Initializing Sensor Stream...")
    env_type = "Environmental Data:temp:humidity:pressure"
    sens_001 = SensorStream("SENSOR_001", env_type)
    s_data = sens_001.process_batch(data_batch)
    print(f"Stream ID: {sens_001.id}, Type: {sens_001.type}")
    print(f"Processing sensor batch: [{s_data}]")
    print(f"Sensor analysis: {len(sens_001.data)} readings processed, "
          f"avg tmp: {sens_001.get_stats()['temp']}")

    print("\nInitializing Transaction Stream...")
    fin_type = " Financial Data:buy:sell"
    trans_001 = TransactionStream("TRANS_001", fin_type)
    t_data = trans_001.process_batch(data_batch)
    print(f"Stream ID: {trans_001.id}, Type: {trans_001.type}")
    print(f"Processing transaction batch: [{t_data}]")
    net_flow = trans_001.get_stats()
    print(f"Transaction analysis: {len(trans_001.data)} operations, net flow: "
          f"{'+' if net_flow['net_flow'] > 0 else ''}{net_flow['net_flow']} units")

    print("\nInitializing Event Stream...")
    eve_type = "System Even:login:error:logout"
    even_001 = EventStream("EVENT_001", eve_type)
    e_data = even_001.process_batch(data_batch)
    print(f"Stream ID: {even_001.id}, Type: {even_001.type}")
    print(f"Processing event batch: [{e_data}]")
    n_error = even_001.get_stats()["error"]
    print(f"Event analysis: {len(even_001.data)} events, {n_error} error detected")
