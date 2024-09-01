import pygame

COR_PLAYER = (0, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(COR_PLAYER)
        self.rect = self.image.get_rect()
        self.rect.topleft = (500, 375)

    def update(self, largura, altura):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            new_x = self.rect.x - 5
            if(new_x <= largura and new_x >= 0):
                self.rect.x -= 5
        if teclas[pygame.K_RIGHT]:
            new_x = self.rect.x + 5
            if(new_x+5 < largura and new_x >= 0):
                self.rect.x += 5
        if teclas[pygame.K_UP]:
            new_y = self.rect.y - 5
            if(new_y <= altura and new_y >= 0):
                self.rect.y -= 5
        if teclas[pygame.K_DOWN]:
            new_y = self.rect.y + 5
            if(new_y+5 < altura and new_y >= 0):
                self.rect.y += 5
