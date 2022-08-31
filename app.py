import pygame


class App:
    def __init__(self):
        self._running = False
        color = (0, 0, 255)
        self.size = self.width, self.height = 100, 100
        self._display_surf = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            print("shit happened")
            self._running = False
        while self._running:
            for event in pygame.event.get():
                print("Event happened")
        self.on_cleanup()


if __name__ == '__main__':
    application = App()
    application.on_execute()
