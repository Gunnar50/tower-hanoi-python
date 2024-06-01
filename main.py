import pygame
from settings import *
from sprites import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.debug = {}
        self.towers = Towers()

    def debug_info(self):
        pass

    def new(self):
        pass

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.debug_info()

    def draw(self):
        self.screen.fill(BGCOLOUR)
        get_info(self.debug)

        self.towers.draw(self.screen)

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                self.towers.events(mx, my)


if __name__ == "__main__":
    game = Game()
    while True:
        game.new()
        game.run()
