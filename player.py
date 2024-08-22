import pygame
import random

COR_PLAYER = (0, 255, 0)

# Definir a classe Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(COR_PLAYER)
        self.rect = self.image.get_rect()
        self.rect.topleft = (500, 375)

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 5
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 5
        if teclas[pygame.K_UP]:
            self.rect.y -= 5
        if teclas[pygame.K_DOWN]:
            self.rect.y += 5
