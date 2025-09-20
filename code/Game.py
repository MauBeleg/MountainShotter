import pygame
from code import Const
from code.Menu import Menu

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(Const.WIN_WIDTH, Const.WIN_HEIGHT))


    def Run(self, ):

        while True:
            menu = Menu(self.window)
            menu.Run()
            pass


