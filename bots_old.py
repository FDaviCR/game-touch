import pygame
from random import randint

# Configurações de bot
speed = 5
bot_size = 25
bot = (0, 255, 0)

# Criar bots
def create_bot(screen, screen_height, screen_width):
    x = randint(20, screen_width)
    y = randint(20, screen_height)

    pygame.draw.circle(screen, bot, [x, y], 15)