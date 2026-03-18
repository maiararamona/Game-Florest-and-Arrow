import pygame.image
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/NovoMenu.png').convert_alpha()
        #self.surf = pygame.transform.scale(self.surf, (576, 324))
        self.rect = self.surf.get_rect(left=0, top=0)
        self.menu_option = 0

    def run(self):
        pygame.mixer_music.load('./asset/somMenu.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(45, text="Florest", text_color=(255, 0, 0), text_center_pos=((576 // 2), 50))
            self.menu_text(45, text="Arrow", text_color=(255, 0, 0), text_center_pos=((576 // 2), 100))

            for i in range(len(MENU_OPTION)):
                if i == self.menu_option:
                    self.menu_text(15, MENU_OPTION[i], (225, 225, 0),
                                   text_center_pos=((576 // 2), 150 + (i * 30)))

                else:
                    self.menu_text(15, MENU_OPTION[i], (0, 0, 50),
                                   text_center_pos=((576 // 2), 150 + (i * 30)))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN: # ceta para baixo
                            if self.menu_option < len(MENU_OPTION) -1:
                                self.menu_option  += 1
                            else:
                                self.menu_option = 0

                        if event.key == pygame.K_UP: # seta para cima
                            if self.menu_option > 0:
                                self.menu_option -= 1
                            else:
                                self.menu_option = len(MENU_OPTION) -1
                        if event.key == pygame.K_RETURN: #EENTER
                            select = self.menu_option
                            self.menu_option = 0
                            return MENU_OPTION[select]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
