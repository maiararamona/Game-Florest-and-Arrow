import sys
import pygame
import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.entity import entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[entity] = []
        self.entity_list.extend(EntityFactory.get_entity('floresta1'))
        self.player = EntityFactory.get_entity('0_Forest_Ranger_passo1', (50, 180))
        self.entity_list.append(self.player)
        self.entity_list.append(EntityFactory.get_entity('0_Orc_passo1', (460, 180)))
        self.clock = pygame.time.Clock()

    def run(self):
        pygame.mixer_music.load(f'./asset/somJogo.wav')
        pygame.mixer_music.play(-1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.window.fill((0, 0, 0))

            for ent in self.entity_list:
                ent.move()
                ent.draw(self.window)

                if hasattr(ent, 'arrows'):
                    for arrow in ent.arrows[:]:
                        arrow.draw(self.window)
                        if arrow.rect.colliderect(self.player.rect):
                            self.player.take_damage(10)
                            ent.arrows.remove(arrow)
                        elif arrow.rect.right < 0 or arrow.rect.left > 576:
                            ent.arrows.remove(arrow)

            self.draw_health_bar()

            if self.player.is_dead():
                result = self.game_over_screen()
                if result == 'restart':
                    self.__init__(self.window, self.name, self.game_mode)  # reinicia
                else:
                    return

            self.level_text(14, f'fps: {self.clock.get_fps():.0f}', (255, 255, 255), (10, 5))
            pygame.display.flip()
            self.clock.tick(60)

    def game_over_screen(self):
        """Tela de game over com opção de reiniciar ou sair."""
        font_big = pygame.font.SysFont("Lucida Sans Typewriter", 40)
        font_small = pygame.font.SysFont("Lucida Sans Typewriter", 20)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return 'restart'
                    if event.key == pygame.K_ESCAPE:
                        return 'quit'

            self.window.fill((0, 0, 0))

            # textos
            text1 = font_big.render("GAME OVER", True, (220, 0, 0))
            text2 = font_small.render("R  - Reiniciar", True, (255, 255, 255))
            text3 = font_small.render("ESC - Sair", True, (255, 255, 255))

            self.window.blit(text1, text1.get_rect(center=(288, 130)))
            self.window.blit(text2, text2.get_rect(center=(288, 190)))
            self.window.blit(text3, text3.get_rect(center=(288, 220)))

            pygame.display.flip()
            self.clock.tick(60)

    def draw_health_bar(self):
        bar_width = 150
        bar_height = 16
        fill = int((self.player.health / 100) * bar_width)
        pygame.draw.rect(self.window, (180, 0, 0), (10, 300, bar_width, bar_height), border_radius=4)
        pygame.draw.rect(self.window, (0, 200, 0), (10, 300, fill, bar_height), border_radius=4)
        self.level_text(13, f'HP: {self.player.health}', (255, 255, 255), (170, 300))

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(topleft=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)