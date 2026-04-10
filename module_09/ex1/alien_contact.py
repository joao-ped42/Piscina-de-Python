try:
    from pydantic import BaseModel, Field, model_validator
except ModuleNotFoundError:
    print("Use pip intall pydantic")
    exit(1)

from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    radio = 1
    visual = 2
    physical = 3
    telepathic = 4


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validation(self) -> 'AlienContact':
        if (self.contact_id[0:2] != "AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if ((self.contact_type.name == "physical") and
                (self.is_verified is None)):
            raise ValueError("A physical contact must be veified")
        if ((self.contact_type.name == "telepathic") and
                (self.witness_count < 3)):
            raise ValueError("That's not enough witnesses")
        if ((self.signal_strength > 7) and (self.message_received is None)):
            raise ValueError("A strong telepathic contact like that "
                             "must have an message")
        return (self)


def display_AC(AC: AlienContact) -> None:
    print(f"ID: {AC.contact_id}")
    print(f"Type: {AC.contact_type.name.capitalize()}")
    print(f"Location: {AC.location}")
    print(f"Signal: {AC.signal_strength:.1f}/10")
    print(f"Duration: {AC.duration_minutes} minutes")
    print(f"Witnesses: {AC.witness_count}")
    if (not (AC.message_received is None)):
        print(f"Message: {AC.message_received}")


def main() -> None:
    print("=============================")
    house: str = "Santa Cruz da Serra, Duque de Caxias - RJ"
    try:
        contact1 = AlienContact(contact_id="AC123",
                                timestamp="2005-11-07T18:30:00",
                                location=house,
                                contact_type=ContactType(1),
                                signal_strength=3,
                                duration_minutes=67,
                                witness_count=1,
                                mensage_received="Busquem comer cimento",
                                is_verified=True)
        print("Valid contact report:")
        display_AC(contact1)
    except Exception as e:
        print(e)
    print("\n=============================")
    try:
        contact2 = AlienContact(contact_id="AC123",
                                timestamp="2005-11-07T18:30:00",
                                location=house,
                                contact_type=ContactType(4),
                                signal_strength=3,
                                duration_minutes=67,
                                witness_count=1,
                                mensage_received="Busquem comer cimento",
                                is_verified=True)
        display_AC(contact2)
    except Exception as e:
        print(e)


if (__name__ == "__main__"):
    print("Alien Contact Log Validation")
    main()
