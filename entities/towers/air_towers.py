from entities.towers.base import BaseTower
from damage_type import DamageType


class AirTower(BaseTower):
    def __init__(self, coords, name="AirTower", health=4, speed=4.4):
        super().__init__(name, health, speed, DamageType.Air, coords)
