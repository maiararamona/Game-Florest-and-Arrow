import pygame
import pygame.transform
from code.entity import entity
from code.arrow import Arrow


class Enemy(entity):
    def __init__(self, position: tuple):
        super().__init__('0_Orc_passo1', position)
        self.surf = pygame.transform.scale(self.surf, (80, 120))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.arrows = []
        self.shoot_cooldown = 0

    def move(self):
        # cooldown entre tiros
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        # atira a cada 60 frames (1 segundo)
        if self.shoot_cooldown == 0:
            new_arrow = Arrow((self.rect.left, self.rect.centery))
            self.arrows.append(new_arrow)
            self.shoot_cooldown = 60

        for new_arrow in self.arrows:
            new_arrow.move()