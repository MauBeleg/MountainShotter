import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code import Const


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def Run(self, ):
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer.music.play(-1)

        while True:

            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(70, 'Mountain', Const.COLOR_ORANGE, ((Const.WIN_WIDTH / 2), 50))
            self.menu_text(70, 'Shooter', Const.COLOR_ORANGE, ((Const.WIN_WIDTH / 2), 90))

            for i in range(len(Const.MENU_OPTION)):
                self.menu_text(40, Const.MENU_OPTION[i], Const.COLOR_WHITE, ((Const.WIN_WIDTH / 2), 160 + 30 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
