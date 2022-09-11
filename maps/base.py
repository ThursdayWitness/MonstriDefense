from typing import Optional
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

    def check_cell(self, mouse_pos: tuple[int, int], map_position: Size) -> Optional[tuple[int, int, bool]]:
        x_pos = (mouse_pos[0] - map_position.width) // self._cell.width
        y_pos = (mouse_pos[1] - map_position.height) // self._cell.height
        if map_position.height < mouse_pos[1] < len(self._map) * self._cell.height + map_position.height and map_position.width < mouse_pos[0] < len(self._map[0]) * self._cell.width + map_position.width:
            if self._map[y_pos][x_pos] == '#':
                return x_pos, y_pos, True
            return x_pos, y_pos, False
        return None
