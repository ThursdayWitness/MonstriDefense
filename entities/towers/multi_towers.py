from base import BaseTower
from damage_type import DamageType


class MultiTower(BaseTower):
    def __init__(self, name='Multi Tower', health=5, speed=1):
        super().__init__(name, health, speed, DamageType.Multi)
