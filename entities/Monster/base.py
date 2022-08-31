class DamageType:
    __multi_type = 0
    __ground = 1
    __air = 2

    @staticmethod
    def multi_type() -> int:
        return DamageType.__multi_type

    @staticmethod
    def ground() -> int:
        return DamageType.__ground

    @staticmethod
    def air() -> int:
        return DamageType.__air


class BaseMonster:
    def __init__(self):
        self.__cost: int = 0
        self.__damage: float = 0.0
        self.__damage_type: int = DamageType.multi_type()
        self.__attack_radius: float = 0.0  # wtf we really gonna do MATH to this????????
        self.__attack_intensity: float = 0.0
        self.__level: int = 0

    @property
    def cost(self):
        return self.__cost

    @property
    def damage(self):
        return self.__damage

    @property
    def attack_radius(self):
        return self.__attack_radius

    @property
    def damage_type(self):
        return self.__damage_type

    def sell(self):
        sell_price = self.__cost / 2
        # add money to player's bank and delete monster from field


