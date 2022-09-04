class MainBase:
    def __init__(self):
        self._health: int = 0

    @property
    def health(self):
        return self._health

    def take_damage(self):
        self._health -= 1
