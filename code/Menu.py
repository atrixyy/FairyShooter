#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Rect, Surface
from pygame.font import Font

from code.Const import WIN_WIDTH, C_PINK, MENU_OPTION, C_WHITE, C_YELLOW, C_GRAY, C_GREEN, \
    C_BLACK, C_BROWN, C_BLUE, C_RED


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/Menu.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer.music.load("./asset/Inicio.mp3")
        pygame.mixer.music.play(-1)
        while True:
            #Draw Images
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(200, "Fairy", C_BLUE, ((WIN_WIDTH / 2), 170))
            self.menu_text(170, "Shooter", C_BLUE, ((WIN_WIDTH / 2), 300))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(50, MENU_OPTION[i], C_PINK, ((WIN_WIDTH / 2), 600 + i * 60))
                else:
                    self.menu_text(50, MENU_OPTION[i], C_BLUE, ((WIN_WIDTH / 2), 600 + i * 60))
            pygame.display.flip()

            #Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s: #Down Key
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_w: # Up Key
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # Enter
                        return MENU_OPTION[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)



