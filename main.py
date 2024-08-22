import pygame
import random
import time

from player import Player
from bot import Bot

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))

# Definir as cores
COR_FUNDO = (30, 30, 30)

# Criar instâncias
player = Player()

# Gerar vários bots e adicioná-los a um array
bots = []

# Criar grupos de sprites
todos_sprites = pygame.sprite.Group()
todos_sprites.add(player)
#todos_sprites.add(bots)  # Adicionar todos os bots ao grupo de sprites

# Variável para controlar o tempo de criação dos bots
ultimo_tempo_bot = time.time()

# Loop principal
executando = True
clock = pygame.time.Clock()

while executando:
    clock.tick(60)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Atualizar os sprites
    todos_sprites.add(bots)
    todos_sprites.update()

    # Verificar colisões entre o player e cada bot
    for bot in bots:
        if player.rect.colliderect(bot.rect):
            print(f"Colisão com: {bot.nome}")
    
    # Criar um novo bot a cada 3 segundos
    if (time.time() - ultimo_tempo_bot > 3) and len(bots) < 5:
        novo_bot = Bot(random.randint(0, largura-50), random.randint(0, altura-50), str(time.time()))
        bots.append(novo_bot)
        ultimo_tempo_bot = time.time()

    # Desenhar o fundo e os sprites
    tela.fill(COR_FUNDO)
    todos_sprites.draw(tela)

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o Pygame
pygame.quit()
