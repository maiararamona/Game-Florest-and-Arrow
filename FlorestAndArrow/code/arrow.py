import pygame
from code.entity import entity


class Arrow(entity):
    def __init__(self, position: tuple, direction: int = -1):
        super().__init__('flecha', position)
        self.surf = pygame.transform.scale(self.surf, (60, 25))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 7
        self.direction = direction

    def move(self):
        self.rect.x += self.speed * self.direction