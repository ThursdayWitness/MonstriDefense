from enum import Flag, auto


class DamageType(Flag):
    Ground = auto()
    Air = auto()
    Multi = Ground | Air
