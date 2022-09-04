from typing import Union

from damage_type import Multi, Air, Ground
from entities.game_object import GameObject


class BaseTower(GameObject):
    def __init__(self, name: str, health: int, speed: float, damage_type: Union[Multi, Air, Ground]):
        super().__init__()
        self._name: str = name
        self._speed: float = speed
        self._health: int = health
        self._damage_type = damage_type

    @property
    def name(self):
        return self._name

    @property
    def speed(self):
        return self._speed

    @property
    def health(self):
        return self._health

    @property
    def damage_type(self):
        return self._damage_type

    def take_damage(self, damage):
        self._health -= damage


# def attack_base(self):
# MainBase.take_damage()  # wtf with self


class AirTower(BaseTower):
    def __init__(self, name="AirTower", health=4, speed=4.4):
        super().__init__(name, health, speed, Air())
        # self._speed = "sdfjsdklfjs"


class GroundTower(BaseTower):
    def __init__(self, name="GroundTower", health=10, speed=2.2):
        super().__init__(name, health, speed, Ground())


class MultiTower(BaseTower):
    def __init__(self, name='Multi Tower', health=5, speed=1):
        super().__init__(name, health, speed, Multi())
