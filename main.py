import pygame
import sys

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

# Configuração do quadrado
square_size = 25
x = screen_width // 2 - square_size // 2  # posição inicial x (centro da tela)
y = screen_height // 2 - square_size // 2  # posição inicial y (centro da tela)
speed = 5  # velocidade do movimento

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
    keys = pygame.key.get_pressed()

    # Movimenta o quadrado
    if keys[pygame.K_LEFT] and x - speed > 0:
        x -= speed  # Move para a esquerda
    if keys[pygame.K_RIGHT] and x + speed < screen_width - square_size:
        x += speed  # Move para a direita
    if keys[pygame.K_UP] and y - speed > 0:
        y -= speed  # Move para cima
    if keys[pygame.K_DOWN] and y + speed < screen_height - square_size:
        y += speed  # Move para baixo

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de quadros (FPS)
    pygame.time.Clock().tick(60)

# Encerra o Pygame
pygame.quit()
sys.exit()
