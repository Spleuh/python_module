from enum import Enum
from pydantic import (BaseModel, Field, model_validator,  # type: ignore
                      ValidationError)
from datetime import datetime
from typing import Callable, Any
import os
import json


class Rank(Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True

    def print_info(self) -> None:
        print(f"- {self.name} ({self.rank.value}) - {self.specialization}")


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = 'planned'
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def custom_validator(self) -> 'SpaceMission':
        if not self.mission_id[0:1] == 'M':
            raise ValueError(f"ID must start with 'M': {self.mission_id}")
        lst_crew_rank = [member.rank.value for member in self.crew]
        set_model = {Rank.CAPTAIN.value, Rank.COMMANDER.value}
        set_rank_crew = set(lst_crew_rank)
        if not set_model.intersection(set_rank_crew):
            raise ValueError(
                "Must have at least one Commander or Captain")
        experienced = [
            member for member in self.crew if member.years_experience > 5]
        if len(experienced) < len(lst_crew_rank) // 2:
            raise ValueError(
                "Long missions (> 365 days) "
                "need 50% experienced crew (5+ years)")
        lst_active = [member.is_active for member in self.crew]
        if not all(lst_active):
            raise ValueError("All crew members must be active")
        return self

    def print_info(self) -> None:
        print('=========================================')
        print('Valid mission created:')
        print(f"Mission: {self.mission_name}")
        print(f"ID: {self.mission_id}")
        print(f"Destination: {self.destination}")
        print(
            f"Duration: {self.duration_days} "
            f"{'day' if self.duration_days == 1 else 'days'}")
        print(f"Budget: ${self.budget_millions}M")
        print(f"Crew size: {len(self.crew)}")
        print('Crew members:')
        for member in self.crew:
            member.print_info()
        print('\n=========================================')


def safe_exec(f: Callable, **kwargs: Any) -> Any:
    try:
        return f(**kwargs)
    except ValidationError as e:
        print("ValidationError:")
        for i in range(len(e.errors())):
            print(f"{e.errors()[i]['msg']}")
        return None
    except Exception as e:
        print(f"{e}")
        return None


def main() -> None:
    print('Space Mission Crew Validation')
    data_path1 = os.path.abspath('generated_data/space_missions.json')
    data_path2 = os.path.abspath('../generated_data/space_missions.json')
    data_path = data_path1 if os.path.exists(data_path1) else data_path2
    if not os.path.exists(data_path):
        print('Generate data with data exporter')
        exit()
    with open(data_path, 'r') as f:
        data = json.load(f)
    if data:
        for i in data:
            tmp = safe_exec(SpaceMission, **i)
            if tmp:
                tmp.print_info()
    invalid_data = {
        "mission_id": "M2024_TITAN",
        "mission_name": "Solar Observatory Research Mission",
        "destination": "Solar Observatory",
        "launch_date": "2024-03-30T00:00:00",
        "duration_days": 451,
        "crew": [
            {
                "member_id": "CM001",
                "name": "Sarah Williams",
                "rank": "captain",
                "age": 43,
                "specialization": "Mission Command",
                "years_experience": 19,
                "is_active": False
            },
            {
                "member_id": "CM002",
                "name": "James Hernandez",
                "rank": "captain",
                "age": 43,
                "specialization": "Pilot",
                "years_experience": 30,
                "is_active": True
            },
            {
                "member_id": "CM003",
                "name": "Anna Jones",
                "rank": "cadet",
                "age": 35,
                "specialization": "Communications",
                "years_experience": 15,
                "is_active": True
            },
            {
                "member_id": "CM004",
                "name": "David Smith",
                "rank": "commander",
                "age": 27,
                "specialization": "Security",
                "years_experience": 15,
                "is_active": True
            },
            {
                "member_id": "CM005",
                "name": "Maria Jones",
                "rank": "cadet",
                "age": 55,
                "specialization": "Research",
                "years_experience": 30,
                "is_active": True
            }
        ],
        "mission_status": "planned",
        "budget_millions": 2208.1
    }

    tmp = safe_exec(SpaceMission, **invalid_data)
    if tmp:
        tmp.print_info()


if __name__ == '__main__':
    main()
