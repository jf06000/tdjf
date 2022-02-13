# This is a sample Python script.
import pygame

from level import Level
from tdsprite import *
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("tower defense")
    lvl1 = Level(screen)
    TdSprite.level = lvl1
    clock = pygame.time.Clock()
    carryOn = True
    while carryOn:

                # First, clear the screen to white.

        # The you can draw different shapes and lines or add text to your background stage.
        #pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
        #pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
        #pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)
        carryOn = lvl1.update()

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    pygame.quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
