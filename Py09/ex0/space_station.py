from pydantic import BaseModel, Field, ValidationError  # type: ignore
from datetime import datetime
from typing import Optional, Callable, Any
import os
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
        print('\nValidationError: ')
        for i in range(len(e.errors())):
            print(f'{e.errors()[i]["msg"]}')
        return None
    except Exception as e:
        print(f'{e}')
        return None


def print_station(station: SpaceStation) -> None:
    print('========================================')
    print('Valid station created:')
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print("Status: "
          f"{'Operational' if station.is_operational else 'Not operational'}")
    print('========================================\n')


def main() -> None:
    print('Space Station Data Validation')
    data_path1 = os.path.abspath('generated_data/space_stations.json')
    data_path2 = os.path.abspath('../generated_data/space_stations.json')
    inv_data_path1 = os.path.abspath('generated_data/invalid_stations.json')
    inv_data_path2 = os.path.abspath('../generated_data/invalid_stations.json')
    data_path = data_path1 if os.path.exists(data_path1) else data_path2
    inv_data_path = (inv_data_path1 if os.path.exists(inv_data_path1)
                     else inv_data_path2)
    if not os.path.exists(data_path) or not os.path.exists(inv_data_path):
        print('Generate data with data exporter')
        exit()
    with open(data_path, 'r') as f:
        valid_data = json.load(f)
    if valid_data:
        for i in valid_data:
            tmp = safe_exec(SpaceStation, **i)
            if tmp:
                print_station(tmp)
    with open(inv_data_path, 'r') as f:
        invalid_data = json.load(f)
    if invalid_data:
        for data in invalid_data:
            tmp = safe_exec(SpaceStation, **data)
            if tmp:
                print_station(tmp)


if __name__ == '__main__':
    main()
