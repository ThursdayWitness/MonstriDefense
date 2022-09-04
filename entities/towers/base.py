from typing import Optional, Union

from damage_type import Multi, Air, Ground
from entities.game_object import GameObject
from entities.main_base import MainBase


class BaseTower(GameObject):
    def __init__(self, name: str, health: int, speed: float, damage_type: Union[Multi, Air, Ground]):
        super().__init__()
        self._name: str = name
        self._speed: float = speed
        self._health: int = health
        self._damage_type: Union[Multi, Air, Ground] = damage_type

    @property
    def name(self):
        return self._name

    @property
    def speed(self):
        return self._speed

    @property
    def health(self):
        return self._health

    def take_damage(self, damage):
        self._health -= damage

    @property
    def type(self):
        return self._damage_type

   # def attack_base(self):
        #MainBase.take_damage()  # wtf with self


class AirTower(BaseTower):
    def __init__(self):
        super().__init__("AirTower", 4, 4.4, Air)
        self._speed = "sdfjsdklfjs"
