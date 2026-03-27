from enum import Enum
from pydantic import (BaseModel, model_validator, Field,  # type: ignore
                      ValidationError)
from datetime import datetime
from typing import Optional, Callable, Any
import os
import json


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=100.0)
    duration_minutes: int = Field(ge=0, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def custom_validator(self) -> 'AlienContact':
        if not self.contact_id[0:2] == 'AC':
            raise ValueError(f"ID must start with 'AC': {self.contact_id}")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact must be verified': "
                             f"{self.contact_type.value} {self.is_verified}")
        if (self.contact_type == ContactType.TELEPATHIC and
                self.witness_count < 3):
            raise ValueError("Telephatic contact requires at "
                             "least 3 witnesses': "
                             f"{self.contact_type.value} {self.witness_count}")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(f"Strong signals should include "
                             f"reveived messages: {self.signal_strength} "
                             f"{self.message_received}")
        return self

    def print_var(self) -> None:
        print('======================================')
        print('Valid contact report:')
        print(f'ID: {self.contact_id}')
        print(f'Type: {self.contact_type.value}')
        print(f'Location: {self.location}')
        print(f'Signal: {self.signal_strength}/10')
        print(f"Duration: {self.duration_minutes} "
              f"{'minute' if self.duration_minutes < 2 else 'minutes'}")
        print(f'Witnesses: {self.witness_count}')
        print(f'Message: {self.message_received}')
        print('\n======================================')


def safe_exec(f: Callable, **kwargs: Any) -> Any:
    try:
        return f(**kwargs)
    except ValidationError as e:
        print('ValidationError')
        for i in range(len(e.errors())):
            print(f"{e.errors()[i]['msg']}")
        return None
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None


def main() -> None:
    print('Alien Contact Log Validation')
    data_path1 = os.path.abspath('generated_data/alien_contacts.json')
    data_path2 = os.path.abspath('../generated_data/alien_contacts.json')
    data_path = data_path1 if os.path.exists(data_path1) else data_path2
    inv_data_path1 = os.path.abspath('generated_data/invalid_contacts.json')
    inv_data_path2 = os.path.abspath('../generated_data/invalid_contacts.json')
    inv_data_path = (inv_data_path1 if os.path.exists(inv_data_path1)
                     else inv_data_path2)
    if not os.path.exists(data_path) or not os.path.exists(inv_data_path):
        print('Generate data with data exporter')
        exit()

    with open(data_path, 'r') as f:
        data = json.load(f)
    if data:
        for i in data:
            tmp = safe_exec(AlienContact, **i)
            if tmp:
                tmp.print_var()

    with open(inv_data_path, 'r') as f:
        invalid_data = json.load(f)
    if invalid_data:
        for i in invalid_data:
            tmp = safe_exec(AlienContact, **i)
        if tmp:
            print('invalid')
            tmp.print_var()


if __name__ == '__main__':
    main()
