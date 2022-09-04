from dataclasses import dataclass


@dataclass
class Multi:
    damage = 0


@dataclass
class Ground:
    damage = 1


@dataclass
class Air:
    damage = 2


    # @staticmethod
    # def multi_type() -> int:
    #     return DamageType.__multi_type
    #
    # @staticmethod
    # def ground() -> int:
    #     return DamageType.__ground
    #
    # @staticmethod
    # def air() -> int:
    #     return DamageType.__air

