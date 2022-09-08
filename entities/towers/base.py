import pygame

from damage_type import DamageType
from entities.game_object import GameObject


class BaseTower(GameObject):
    def __init__(self, name: str, health: int, speed: float, damage_type: DamageType, coords: tuple[int, int]):
        super().__init__()
        self._name: str = name
        self._speed: float = speed
        self._health: int = health
        self._damage_type: DamageType = damage_type
        self._coords: tuple[int, int] = coords

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

    def topat(self):
        pass



# def attack_base(self):
# MainBase.take_damage()  # wtf with self







