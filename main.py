import pygame
import sys
import time

from player import move_player_in_screen
from bots import create_bot

# Inicializa o Pygame
pygame.init()

# Configuração da tela
screen_width = 1000
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Touch')

# Definir cores
background = (0, 0, 0)
player = (255, 0, 0)

# Configuração do player
square_size = 25
x = screen_width // 2 - square_size // 2  # posição inicial x (centro da tela)
y = screen_height // 2 - square_size // 2  # posição inicial y (centro da tela)

# Loop principal
running = True
ultimo_tempo = time.time()

while running:
    # Preenche a cor de fundo da tela
    screen.fill(background)

    # Desenha o quadrado na nova posição
    pygame.draw.rect(screen, player, [x, y, square_size, square_size])
    
    # Lida com eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Desenha um novo bot        
    if time.time() - ultimo_tempo > 5:
        create_bot(screen, screen_height, screen_width)
        ultimo_tempo = time.time()
            
    # Movimentos do player
    updatePositionPlayer = move_player_in_screen(x, y, screen_width, screen_height, square_size)
    x = updatePositionPlayer[0]
    y = updatePositionPlayer[1]
        
    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de quadros (FPS)
    pygame.time.Clock().tick(60)

# Encerrar o Pygame
pygame.quit()
sys.exit()
