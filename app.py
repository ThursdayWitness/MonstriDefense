import pygame

from windows import zastavka


class App:
    def __init__(self):
        self._running = False
        self.size = self.width, self.height = 720, 640
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
        zastavka.run_zastavka(self._display_surf)
        while self._running:
            for event in pygame.event.get():
                print("Event happened")
                pygame.display.update()

        self.on_cleanup()


if __name__ == '__main__':
    #application = App()
    #application.on_execute()
    gavno = towers.BaseTower("Base", 1, 1.0)
    gavno1 = towers.AirTower()
    gavno2 = towers.GroundTower()

    govnar = monsters.BaseMonster("Base", 10, 1.1, 1.1, 1.1)
    govnar1 = monsters.PVO()
    govnar2 = monsters.Catapult()

    if govnar.damage_type == gavno2.damage_type:
        print("Ebanulo konkretno")
    else:
        print("Huy tam, ne popast")