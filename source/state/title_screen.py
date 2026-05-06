import pygame as pg
from .. import constants as c
from ..tool import State

class TitleScreen(State):
    def __init__(self):
        super().__init__()
        self.next = c.MAIN_MENU

        # Load full-screen background image
        self.background = pg.image.load("resources/graphics/Screen/title_background1.png").convert()
        self.background = pg.transform.smoothscale(self.background, (c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

    def startup(self, current_time, persist):
        self.start_time = current_time
        self.persist = persist

    def update(self, surface, current_time, mouse_pos, mouse_click):
        # Draw background image
        surface.blit(self.background, (0, 0))


        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN]:
            self.done = True
