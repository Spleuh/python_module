from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional, Callable, Any
from data_exporter import SpaceStationGenerator, DataConfig, create_test_scenarios
import json


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)



def safe_exec(f: Callable, **kwargs: Any) -> Any:
    try:
        return f(**kwargs)
    except ValidationError as e:
        print(f'ValidationError: \n{e}\n')
        return None
    except Exception as e:
        print(f'{e}')
        return None


def print_station(station: SpaceStation):
    print('========================================')
    print('Valid station created:')
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {'Operational' if station.is_operational else 'Not operational'}")
    print('========================================\n')


def main():
    print('Space Station Data Validation')
    data_generator = SpaceStationGenerator(DataConfig())
    lst_data = data_generator.generate_station_data()
    create_test_scenarios()
    for i in lst_data:
        tmp = safe_exec(SpaceStation, **i)
        if tmp:
            print_station(tmp)
    with open('generated_data/invalid_stations.json', 'r') as f:
        invalid_data = json.load(f)
    if invalid_data:
        for data in invalid_data:
            tmp = safe_exec(SpaceStation, **data)
            if tmp:
                print_station(tmp)


if __name__ == '__main__':
    main()