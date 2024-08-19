import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 5
        self.largura = 50
        self.altura = 50
        self.cor_player = (0, 255, 0)

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor_player, (self.x, self.y, self.largura, self.altura))

    def mover(self, teclas, largura, altura):
        if teclas[pygame.K_LEFT] and self.x - self.velocidade > 0:
            self.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.x + self.largura + self.velocidade < largura:
            self.x += self.velocidade
        if teclas[pygame.K_UP] and self.y - self.velocidade > 0:
            self.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.y + self.altura + self.velocidade < altura:
            self.y += self.velocidade
