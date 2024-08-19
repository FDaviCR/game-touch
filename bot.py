import pygame
import random

class Bot:
    def __init__(self, x, y, velocidade):
        self.x = x
        self.y = y
        self.velocidade = velocidade
        self.largura = 50
        self.altura = 50
        self.cor_bot = (255, 0, 0)

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor_bot, (self.x, self.y, self.largura, self.altura))

    def mover(self, largura, altura):
        direcao = random.choice(['left', 'right', 'up', 'down'])
        if direcao == 'left' and self.x - self.velocidade > 0:
            self.x -= self.velocidade
        if direcao == 'right' and self.x + self.largura + self.velocidade < largura:
            self.x += self.velocidade
        if direcao == 'up' and self.y - self.velocidade > 0:
            self.y -= self.velocidade
        if direcao == 'down' and self.y + self.altura + self.velocidade < altura:
            self.y += self.velocidade
