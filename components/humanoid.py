from enum import Enum


class Races(Enum):
    Human = 1,
    Goblin = 2,
    Orc = 3,
    Troll = 4


class Professions(Enum):
    Fighter = 1,
    Rogue = 2,
    Mage = 3,
    Monster = 4


class Humanoid:
    def __init__(self, race, profession, level):
        self.race = race
        self.profession = profession
        self.level = level
