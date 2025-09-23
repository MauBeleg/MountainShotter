from code import Const
from code.Entity import Entity


class Background(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= Const.ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = Const.WIN_WIDTH
        pass