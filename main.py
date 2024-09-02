import pygame
import random
import time

from player import Player
from bot import Bot

pygame.init()

largura, altura = 1000, 750
tela = pygame.display.set_mode((largura, altura))

COR_FUNDO = (30, 30, 30)

player = Player()

bots = []

todos_sprites = pygame.sprite.Group()
todos_sprites.add(player)

ultimo_tempo_bot = time.time()

executando = True
clock = pygame.time.Clock()

while executando:
    clock.tick(60)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    todos_sprites.add(bots)
    todos_sprites.update(largura, altura)

    for bot in bots:
        if player.rect.colliderect(bot.rect):
            print(f"Colisão com: {bot.nome}")
            todos_sprites.remove(bot)
            bots.remove(bot)
            
    
    if (time.time() - ultimo_tempo_bot > 3) and len(bots) < 10:
        novo_bot = Bot(random.randint(0, largura-50), random.randint(0, altura-50), str(time.time()))
        bots.append(novo_bot)
        ultimo_tempo_bot = time.time()

    tela.fill(COR_FUNDO)
    todos_sprites.draw(tela)

    pygame.display.flip()

pygame.quit()
