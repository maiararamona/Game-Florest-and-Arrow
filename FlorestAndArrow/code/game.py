from code.menu import Menu
from code.level import Level
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324))

    def run(self):
        menu = Menu(self.window)
        while True:
            menu_return = menu.run()

            if menu_return == 'PLAY':
                level = Level(self.window, 'floresta1', menu_return)
                level.run()
            elif menu_return == 'EXIT':
                pygame.quit()
                quit()