from typing import Union

from pygame import Surface
from pygame.mixer import music
from pygame.surface import SurfaceType


def run_zastavka(display: Union[Surface, SurfaceType]):
    display.fill((0, 0, 255))
    play_music("sounds/music/bashenki_ost.ogg")

def play_music(path: str):
    music.load(path)  # sounds/music/bashenki_ost.ogg
    music.play(-1)


