import pygame
import random
import time

from player import Player
from bot import Bot

pygame.init()

largura, altura = 1000, 600
tela = pygame.display.set_mode((largura, altura))
points = 0

COR_FUNDO = (30, 30, 30)
COR_FONTE = (255, 255, 255)
player = Player()

bots = []

todos_sprites = pygame.sprite.Group()
todos_sprites.add(player)

ultimo_tempo_bot = time.time()

executando = True
clock = pygame.time.Clock()

font = pygame.font.SysFont("Comic Sans", 25)
score = 0
start_time = time.time()

def showScore():
    scoreText = font.render("Pontos: " + str(score), True, COR_FONTE)
    tela.blit(scoreText, (150, 0))
    
def showTimer():
    elapsedTime = time.time() - start_time
    hours, remainder = divmod(elapsedTime, 3600)
    minutes, seconds = divmod(remainder, 60)
    scoreText = font.render(str(f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"), True, COR_FONTE)
    tela.blit(scoreText, (700, 0))

while executando:
    clock.tick(60)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    todos_sprites.add(bots)
    todos_sprites.update(largura, altura)

    for bot in bots:
        if player.rect.colliderect(bot.rect):
            score += 1
            todos_sprites.remove(bot)
            bots.remove(bot)
            
    
    if (time.time() - ultimo_tempo_bot > 3) and len(bots) < 10:
        novo_bot = Bot(random.randint(0, largura-50), random.randint(0, altura-50), str(time.time()))
        bots.append(novo_bot)
        ultimo_tempo_bot = time.time()

    tela.fill(COR_FUNDO)
    todos_sprites.draw(tela)

    showScore()
    showTimer()
    pygame.display.flip()

pygame.quit()
