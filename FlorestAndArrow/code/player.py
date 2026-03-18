import pygame
import pygame.transform
from code.entity import entity


class Player(entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.transform.scale(self.surf, (80, 120))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.health = 100
        self.vel_y = 0
        self.on_ground = False
        self.ground_y = position[1]  # posição do chão

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_dead(self):
        return self.health <= 0

    def move(self):
        pressed_key = pygame.key.get_pressed()

        # pular com SPACE ou seta cima
        if (pressed_key[pygame.K_SPACE] or pressed_key[pygame.K_UP]) and self.on_ground:
            self.vel_y = -15
            self.on_ground = False

        # gravidade
        self.vel_y += 0.8
        self.rect.y += int(self.vel_y)

        # chão
        if self.rect.y >= self.ground_y:
            self.rect.y = self.ground_y
            self.vel_y = 0
            self.on_ground = True