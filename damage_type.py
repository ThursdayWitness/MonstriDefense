from dataclasses import dataclass


@dataclass
class Multi:
    pass


@dataclass
class Ground:
    def __eq__(self, other):
        if isinstance(other, Multi) or isinstance(other, Ground):
            return True
        return False


@dataclass
class Air:
    def __eq__(self, other):
        if isinstance(other, Multi) or isinstance(other, Air):
            return True
        return False
