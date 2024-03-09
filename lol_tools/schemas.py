from pydantic import BaseModel
from enum import Enum


class HeroType(Enum):
    ENEMY = 0
    ALLY = 1


class EnemyStatus(Enum):
    EnemyHighHealth = "Enemy_High_Health"
    EnemyLowHealth = "Enemy_Low_Health"
    EnemyMediumHealth = "Enemy_Medium_Health"


class BaseHero(BaseModel):
    name: str
    type: HeroType = HeroType.ENEMY


class Position(BaseModel):
    x1: float  # the x coordinate of the top left corner
    y1: float  # the y coordinate of the top left corner
    x2: float  # the x coordinate of the bottom right corner
    y2: float  # the y coordinate of the bottom right corner

    def get_center(self):
        return (self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2


class HeroPosition(Position):
    hero: BaseHero
    health_type: EnemyStatus
