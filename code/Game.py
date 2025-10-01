import pygame
from code import Const
from code.Menu import Menu
from code.Level import Level

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(Const.WIN_WIDTH, Const.WIN_HEIGHT))


    def Run(self, ):

        while True:
            menu = Menu(self.window)
            menuReturn = menu.Run()

            if menuReturn in [Const.MENU_OPTION[0], Const.MENU_OPTION[1], Const.MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menuReturn)
                levelReturn = level.run()
            elif menuReturn == Const.MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass



