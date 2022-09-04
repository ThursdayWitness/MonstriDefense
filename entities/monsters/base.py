from typing import Union

from damage_type import Air, Ground, Multi


class BaseMonster:
    def __init__(self, name: str, cost: int, damage: float, attack_radius: float,
                 attack_speed: float, damage_type: Union[Multi, Air, Ground]):
        self._name = name
        self._cost = cost
        self._damage = damage
        self._attack_radius = attack_radius  # wtf we really gonna do MATH to this????????
        self._attack_speed = attack_speed
        self._damage_type = damage_type
        self._level = 0

    @property
    def name(self):
        return self._name

    @property
    def cost(self):
        return self._cost

    @property
    def damage(self):
        return self._damage

    @property
    def attack_radius(self):
        return self._attack_radius

    @property
    def attack_speed(self):
        return self._attack_speed

    @property
    def level(self):
        return self._level

    @property
    def damage_type(self):
        return self._damage_type

    # def attack(self):

    def sell(self):
        sell_price = self._cost / 2
        # add money to player's bank and delete monster from field


class AirMonster(BaseMonster):
    def __init__(self, name="PVO", cost=40, damage=1.1, attack_radius=44.44,
                 attack_speed=0.8):
        super().__init__(name, cost, damage, attack_radius, attack_speed, Air())


class GroundMonster(BaseMonster):
    def __init__(self, name="Catapult", cost=20, damage=4, attack_radius=24.44,
                 attack_speed=0.16):
        super().__init__(name, cost, damage, attack_radius, attack_speed, Ground())


class MultiMonster(BaseMonster):
    def __init__(self, name='Multi', cost=10, damage=2, attack_radius=12, attack_speed=1.2):
        super().__init__(name, cost, damage, attack_radius, attack_speed, Multi())
