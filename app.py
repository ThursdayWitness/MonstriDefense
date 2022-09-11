import pygame

from windows import zastavka
from sys import exit
from maps import test_map


class App:
    def __init__(self):
        self._running = False
        self.size = self.width, self.height = 720, 640
        self._screen = None
        self._map = None

    def on_init(self):
        pygame.init()
        self._screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_cleanup(self):
        pygame.quit()
        exit()

    def on_execute(self):
        if self.on_init() == False:
            print("shit happened")
            self._running = False

        # zastavka.run_zastavka(self._screen)
        clock = pygame.time.Clock()
        cell_size = 50
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            white = (255, 255, 255)
            map = test_map.map
            row_count = len(map)
            col_count = len(map[0])
            for i, row in enumerate(map):
                for j, cell in enumerate(row):
                    if map[i][j] == '#':
                        pygame.draw.rect(self._screen, white, pygame.Rect(cell_size + cell_size*j, cell_size+cell_size*i, cell_size, cell_size), 1)

            pygame.display.update()
            clock.tick(60)

        self.on_cleanup()


if __name__ == '__main__':
    application = App()
    application.on_execute()
