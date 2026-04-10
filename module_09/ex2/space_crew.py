try:
    from pydantic import BaseModel, Field, model_validator
except ModuleNotFoundError:
    print("Use pip intall pydantic")
    exit(1)

from datetime import datetime
from enum import Enum


def ft_len(lst: list) -> int:
    count: int = 0
    for _ in lst:
        count += 1
    return (count)


class Rank(Enum):
    commander = 1
    captain = 2
    lieutenant = 3
    officer = 4
    cadet = 5


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=50)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=2, max_length=50)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode='after')
    def validation(self) -> 'SpaceMission':
        if (self.mission_id[0] != 'M'):
            raise ValueError("Invalid Mission ID")
        for crew_member in self.crew:
            if (crew_member.is_active is False):
                raise ValueError(f"{crew_member.name} is inactive")
        valid_crew: bool = False
        for crew_member in self.crew:
            if ((crew_member.rank.name == "commander") or
                    (crew_member.rank.name == "captain")):
                valid_crew = True
        if (valid_crew is False):
            raise ValueError("A mission must have at least one"
                             " Commander or Captain")
        if (self.duration_days > 365):
            for crew_member in self.crew:
                if (crew_member.years_experience < 5):
                    raise ValueError(f"{crew_member.name} is too unexperienced"
                                     " for this mission")
        return (self)


def display_mission(mission: SpaceMission) -> None:
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions:.2f}M")
    print(f"Crew size: {ft_len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        name: str = member.name
        rank: str = member.rank.name.capitalize()
        spec: str = member.specialization
        print(f" - {name} ({rank}) - {spec}")


def main() -> None:
    print("=============================")
    crew1: list = [CrewMember(member_id="2026.5",
                              name="Josebel",
                              rank=Rank(1),
                              age=37,
                              specialization="Teacher",
                              years_experience=37),
                   CrewMember(member_id="2021.67",
                              name="Heather Chandler",
                              rank=Rank(2),
                              age=19,
                              specialization="Cooker",
                              years_experience=7),
                   CrewMember(member_id="1991.1",
                              name="Dio",
                              rank=Rank(4),
                              age=80,
                              specialization="Surgeon",
                              years_experience=8)]
    mission1 = SpaceMission(mission_id="M2026.67",
                            mission_name="Catch the flag",
                            destination="Cabo Frio",
                            launch_date="2005-11-07T18:30:00",
                            duration_days=40,
                            crew=crew1,
                            budget_millions=67)
    print("Valid mission created:")
    display_mission(mission1)
    print("\n=============================")
    try:
        crew2: list = [CrewMember(member_id="2026.5",
                                  name="Naruto",
                                  rank=Rank(4),
                                  age=37,
                                  specialization="Teacher",
                                  years_experience=37),
                       CrewMember(member_id="2021.67",
                                  name="Sakura",
                                  rank=Rank(4),
                                  age=19,
                                  specialization="Cooker",
                                  years_experience=7),
                       CrewMember(member_id="1991.1",
                                  name="Sasuke",
                                  rank=Rank(4),
                                  age=80,
                                  specialization="Surgeon",
                                  years_experience=8)]
        mission2 = SpaceMission(mission_id="M2026.67",
                                mission_name="Catch the flag",
                                destination="Cabo Frio",
                                launch_date="2005-11-07T18:30:00",
                                duration_days=40,
                                crew=crew2,
                                budget_millions=67)
        display_mission(mission2)
    except Exception as e:
        print(e)


if (__name__ == "__main__"):
    print("Space Mission Crew Validation")
    main()
