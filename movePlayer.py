import pygame

speed = 5

def move(x, y, screen_width, screen_height, square_size):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x - speed > 0:
        x -= speed  # Move para a esquerda
    if keys[pygame.K_RIGHT] and x + speed < screen_width - square_size:
        x += speed  # Move para a direita
    if keys[pygame.K_UP] and y - speed > 0:
        y -= speed  # Move para cima
    if keys[pygame.K_DOWN] and y + speed < screen_height - square_size:
        y += speed  # Move para baixo
    
    return [x,y]
        
    