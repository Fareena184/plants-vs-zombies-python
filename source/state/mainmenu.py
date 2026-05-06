

import pygame as pg
from .. import tool
from .. import constants as c

class Menu(tool.State):
    def __init__(self):
        tool.State.__init__(self)

    def startup(self, current_time, persist):
        self.next = c.LEVEL
        self.persist = persist
        self.game_info = persist

        self.setupBackground()
        self.setupOptions()

    def setupBackground(self):
        frame_rect = [80, 0, 800, 600]
        self.bg_image = tool.get_image(tool.GFX[c.MAIN_MENU_IMAGE], *frame_rect)
        self.bg_rect = self.bg_image.get_rect()
        self.bg_rect.x = 0
        self.bg_rect.y = 0

    def setupOptions(self):
        frame_rect = [0, 0, 284, 129]

        # --- Adventure Button ---
        adv_frame_names = [c.OPTION_ADVENTURE + '_0', c.OPTION_ADVENTURE + '_3']
        self.option_frames = []
        for i, name in enumerate(adv_frame_names):
            scale = 1.2 if i == 0 else 1.1
            self.option_frames.append(tool.get_image(tool.GFX[name], *frame_rect, c.BLACK, scale))
        self.option_frame_index = 0
        self.option_image = self.option_frames[self.option_frame_index]
        self.option_rect = self.option_image.get_rect(center=(555, 170))  # Adventure button stays at 140

        # --- Exit Button ---
        exit_frame_names = [c.EXITBUTTON + '_0', c.EXITBUTTON + '_1']
        self.exit_frames = []
        for i, name in enumerate(exit_frame_names):
            scale = 1.2 if i == 0 else 1.0
            self.exit_frames.append(tool.get_image(tool.GFX[name], *frame_rect, c.BLACK, scale))
        self.exit_frame_index = 0
        self.exit_image = self.exit_frames[self.exit_frame_index]
        self.exit_rect = self.exit_image.get_rect(center=(500, 310))  # Positioned below Adventure

        # State tracking
        self.option_start = 0
        self.option_timer = 0
        self.option_clicked = False
        self.exit_clicked = False

    def checkOptionClick(self, mouse_pos):
        x, y = mouse_pos
        if self.option_rect.collidepoint(x, y):
            self.option_clicked = True
            self.option_timer = self.option_start = self.current_time
        elif self.exit_rect.collidepoint(x, y):
            self.exit_clicked = True
            self.option_timer = self.option_start = self.current_time

    def update(self, surface, current_time, mouse_pos, mouse_click):
        self.current_time = self.game_info[c.CURRENT_TIME] = current_time

        if not self.option_clicked and not self.exit_clicked:
            if mouse_click and mouse_pos:
                self.checkOptionClick(mouse_pos)
        else:
            if (self.current_time - self.option_timer) > 200:
                if self.option_clicked:
                    self.option_frame_index = (self.option_frame_index + 1) % 2
                    self.option_image = self.option_frames[self.option_frame_index]
                elif self.exit_clicked:
                    self.exit_frame_index = (self.exit_frame_index + 1) % 2
                    self.exit_image = self.exit_frames[self.exit_frame_index]
                self.option_timer = self.current_time

            if (self.current_time - self.option_start) > 1300:
                if self.option_clicked:
                    self.done = True
                elif self.exit_clicked:
                    pg.quit()
                    exit()

        # Draw everything
        surface.blit(self.bg_image, self.bg_rect)
        surface.blit(self.option_image, self.option_rect)
        surface.blit(self.exit_image, self.exit_rect)
