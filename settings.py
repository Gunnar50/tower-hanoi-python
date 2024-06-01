# COLORS (r, g, b)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTBROWN = (87, 74, 62)
DARKBROWN = (77, 63, 49)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (57, 42, 26)
COLOURS = [RED, GREEN, BLUE, YELLOW, WHITE]

# game settings
BGCOLOUR = LIGHTBROWN
FPS = 60
TITLE = "Tower of Hanoi"
WIDTH = 1200
HEIGHT = 700

DISC_HEIGHT = 30
GAPSIZE = 10

import pygame
pygame.init()
font = pygame.font.Font(None, 25)

def get_info(info_list):
    display_surface = pygame.display.get_surface()
    for i, key in enumerate(info_list):
        text = font.render(str(key) + " : " + str(info_list[key]), True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.x = 700
        text_rect.y = 20 * i
        display_surface.blit(text, text_rect)
