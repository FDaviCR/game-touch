import pygame
import sys

from movePlayer import move

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
while running:
    # Preenche a cor de fundo da tela
    screen.fill(background)

    # Desenha o quadrado na nova posição
    pygame.draw.rect(screen, player, [x, y, square_size, square_size])

    # Lida com eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Captura as teclas pressionadas
    

    # Movimenta o quadrado
    updatePositionPlayer = move(x, y, screen_width, screen_height, square_size)
    x = updatePositionPlayer[0]
    y = updatePositionPlayer[1]
        
    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de quadros (FPS)
    pygame.time.Clock().tick(60)

# Encerra o Pygame
pygame.quit()
sys.exit()
