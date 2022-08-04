import pygame


class Player:
    def __init__(self):
        self.screen = pygame.Surface((50,50))
        self.screen.fill((255,255,255))
        self.x = 0
        self.y = 0
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False

    def update(self):
        if self.mright:
            self.x += 0.1
        if self.mleft:
            self.x -= 0.1
        if self.mup:
            self.y -= 0.1
        if self.mdown:
            self.y += 0.1
