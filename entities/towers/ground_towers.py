from base import BaseTower
from damage_type import DamageType


class GroundTower(BaseTower):
    def __init__(self, name="GroundTower", health=10, speed=2.2):
        super().__init__(name, health, speed, DamageType.Ground)
