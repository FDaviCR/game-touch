import pygame
import random

COR_BOT = (255, 0, 0)

class Bot(pygame.sprite.Sprite):
    def __init__(self, x, y, nome):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(COR_BOT)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.nome = nome  

    def update(self, largura, altura):
        new_x = random.choice([-20, 20])
        new_y = random.choice([-20, 20])
        
        if(new_x + self.rect.x <= largura and self.rect.y + new_y <= altura and new_x + self.rect.x >= 0 and self.rect.y + new_y >= 0):
            self.rect.x += new_x
            self.rect.y += new_y
