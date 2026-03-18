from abc import ABC

from code.entity import entity


class Background(entity, ABC):
    def __init__(self, name, position, speed):
        super().__init__(name, position)
        self.speed = speed
        self.x1 = float(position[0])
        self.x2 = float(self.surf.get_width())


    def move(self):
        self.x1 -= self.speed
        self.x2 -= self.speed

        if self.x1 <= -self.surf.get_width():
            self.x1 = self.x2 + self.surf.get_width()
        if self.x2 <= -self.surf.get_width():
            self.x2 = self.x1 + self.surf.get_width()


    def update(self, window_width):
        self.move()


    def draw(self, window):
        window.blit(self.surf, (int(self.x1), self.rect.y))
        window.blit(self.surf, (int(self.x2), self.rect.y))
