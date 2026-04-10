try:
    from pydantic import BaseModel, Field
except ModuleNotFoundError:
    print("Use pip intall pydantic")
    exit(1)

from datetime import datetime
from typing import Optional


class Station(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None)


def display_station(station: Station) -> None:
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    if (station.is_operational):
        print("Status: Operational")
    else:
        print("Status: Inactive")
    if (station.notes):
        print(f"Notes: {station.notes}")


def main() -> None:
    print("=============================")
    s1: Station = Station(station_id="ISS67",
                          name="Interestellar",
                          crew_size=6,
                          power_level=67.67,
                          oxygen_level=4.20,
                          last_maintenance="2023-10-25T14:30:00",
                          notes="Nada")
    print("Valid station created:")
    display_station(s1)
    print("\n=============================")
    try:
        s2: Station = Station(station_id="ISS67",
                              name="Interestellar",
                              crew_size=30,
                              power_level=67.67,
                              oxygen_level=4.20,
                              last_maintenance="2005-11-07T18:30:00")
        display_station(s2)
    except Exception as e:
        print(e)


if (__name__ == "__main__"):
    print("Space Station Data Validation")
    main()
