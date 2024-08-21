import pygame
import random
import time

from player import Player
from bot import Bot

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da tela
largura, altura = 1000, 700
tela = pygame.display.set_mode((largura, altura))

# Definir cores
COR_FUNDO = (30, 30, 30)
COR_PLAYER = (0, 255, 0)
COR_BOT = (255, 0, 0)

# Definir a taxa de frames por segundo (FPS)
FPS = 60

# Criar o player
player = Player(largura // 2, altura // 2)

# Lista para armazenar os bots
bots = []

# Variável para controlar o tempo de criação dos bots
ultimo_tempo_bot = time.time()

# Loop principal
executando = True
clock = pygame.time.Clock()

while executando:
    clock.tick(FPS)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Capturar teclas pressionadas
    teclas = pygame.key.get_pressed()

    # Mover o player
    player.mover(teclas, largura, altura)
    
    # Mover bots
    for bot in bots:
        bot.mover(largura, altura)

    # Criar um novo bot a cada 3 segundos
    if (time.time() - ultimo_tempo_bot > 3) and len(bots) <= 5:
        novo_bot = Bot(random.randint(0, largura-50), random.randint(0, altura-50), player.velocidade * 5)
        bots.append(novo_bot)
        ultimo_tempo_bot = time.time()
    
    # Preencher a tela com a cor de fundo
    tela.fill(COR_FUNDO)

    # Desenhar o player e bots
    player.desenhar(tela)
    for bot in bots:
        bot.desenhar(tela)

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o Pygame
pygame.quit()
