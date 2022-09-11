import pygame


class Size:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height


class Map:
    def __init__(self, cell_size: Size, cells_map: list[str]):
        self._cell = cell_size
        self._map = cells_map
        self._portal: pygame.Vector2
        self._village: pygame.Vector2

        for i, row in enumerate(cells_map):
            for j, cell in enumerate(row):
                if cell == '@':
                    self._portal = pygame.Vector2(cell_size.width * j, cell_size.height * i)
                if cell == '&':
                    self._village = pygame.Vector2(cell_size.width * j, cell_size.height * i)
        # self._background

    @property
    def cell(self):
        return self._cell

    @property
    def map(self):
        return self._map

    @property
    def portal(self):
        return self._portal

    @property
    def village(self):
        return self._village
