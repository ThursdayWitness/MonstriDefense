from typing import Optional
import pygame
from maps.base import Map, Size
from maps.test_map import build_test_map
from windows import zastavka
from sys import exit
from maps import test_map


class App:
    def __init__(self):
        self._running = False
        self.size = self.width, self.height = 720, 640
        self._screen = None
        self._map: Optional[Map] = None
        self._map_position = Size(10, 10)  # стартовая позиция карты
        self._highlighted_cell = (0, 0)  # последняя посвечиваемая переменная, нужна чтоб убирать отрисовку при смене перемещении курсора

    def on_init(self):
        pygame.init()
        self._screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEMOTION:  # реакция на перемещение курсора
            pos = pygame.mouse.get_pos()
            white = (255, 255, 255)
            black = (0, 0, 0)
            # print(f'x: {pos[0]} |y: {pos[1]}')
            cell = self._map.check_cell(pos, self._map_position)  # проверка входит ли курсор в юзаемый квадрат | неюзаемыей квадрат | вообще в играемую область
            if cell is not None:  # отрисовка квадрата или отрисовка того что мышка уже не над квадратом
                cell_x, cell_y, is_under_mouse = cell
                if cell_x != self._highlighted_cell[0] or cell_y != self._highlighted_cell[1]:
                    pygame.draw.rect(self._screen, black, pygame.Rect(
                        self._map_position.width + self._map.cell.width * self._highlighted_cell[0],
                        self._map_position.height + self._map.cell.height * self._highlighted_cell[1],
                        self._map.cell.width,
                        self._map.cell.height), 0)
                    self._highlighted_cell = (cell_x, cell_y)

                if is_under_mouse:
                    pygame.draw.rect(self._screen, white, pygame.Rect(
                        self._map_position.width + self._map.cell.width * cell_x,
                        self._map_position.height + self._map.cell.height * cell_y,
                        self._map.cell.width,
                        self._map.cell.height), 0)

    def on_cleanup(self):
        pygame.quit()
        exit()

    def on_execute(self):
        if self.on_init() == False:
            print("shit happened")
            self._running = False

        # zastavka.run_zastavka(self._screen)
        clock = pygame.time.Clock()
        self._map = build_test_map()
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            white = (255, 255, 255)

            for i, row in enumerate(self._map.map):
                for j, cell in enumerate(row):
                    if self._map.map[i][j] == '#':
                        pygame.draw.rect(self._screen, white, pygame.Rect(
                            self._map_position.width + self._map.cell.width * j,
                            self._map_position.height + self._map.cell.height * i,
                            self._map.cell.width,
                            self._map.cell.height), 1)

            pygame.display.update()
            clock.tick(60)

        self.on_cleanup()


if __name__ == '__main__':
    application = App()
    application.on_execute()
