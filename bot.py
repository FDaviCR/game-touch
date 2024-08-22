import pygame
import random

COR_BOT = (255, 0, 0)

# Definir a classe Bot
class Bot(pygame.sprite.Sprite):
    def __init__(self, x, y, nome):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(COR_BOT)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.nome = nome  # Nome exclusivo para cada bot

    def update(self):
        # Movimento simples do bot (exemplo)
        self.rect.x += random.choice([-2, 2])
        self.rect.y += random.choice([-2, 2])
