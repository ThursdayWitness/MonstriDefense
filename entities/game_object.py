import pygame


class GameObject:
    def __init__(self):
        self.position = pygame.Vector2(0.0, 0.0)
        self._sprite = pygame.sprite.Sprite()

    # @property
    # def proverka(self):
    #     return self._shit
