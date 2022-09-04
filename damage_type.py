from dataclasses import dataclass

@dataclass
class DamageType(eq=True):
    damage = None

    def __eq__(self, other):
        if other is DamageType:
            return True
        return False

@dataclass
class Multi(DamageType, eq=True):
    damage = 0

    def __eq__(self, other):
        super.__eq__(self, other)

@dataclass
class Ground(DamageType, eq=True):
    damage = 1

    def __eq__(self, other):
        if super.__eq__(self, other):
            if other is Multi or Ground:
                return True

@dataclass
class Air(DamageType, eq=True):
    damage = 2

    def __eq__(self, other):
        if super.__eq__(self, other):
            if other is Multi or Air:
                return True

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

