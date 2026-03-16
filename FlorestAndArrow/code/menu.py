#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from const import MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menuDoJogo.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/somMenu.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, text="Florest", text_color=(255, 128, 0), text_center_pos=((868 // 2), 70))
            self.menu_text(50, text="Arrow", text_color=(255, 128, 0), text_center_pos=((868 // 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], text_color=(255, 255, 255),
                               text_center_pos=((868 // 2), 350 + (i * 50)))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
