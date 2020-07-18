import pygame

from pygame.locals import (
    KEYDOWN,
    K_UP,
    K_DOWN,
    K_RIGHT,
    K_LEFT,
    QUIT,
    K_ESCAPE
)

# CONSTANTS 
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((64, 16))
        self.surf.fill((192, 192, 192))
        self.rect = self.surf.get_rect()
    
    def update(self, keys_pressed):
        if self.rect.bottom < SCREEN_HEIGHT and keys_pressed[K_DOWN]:
            self.rect.move_ip(0, 4)

        if self.rect.top > 0 and keys_pressed[K_UP]:
            self.rect.move_ip(0, -4)

        if self.rect.left > 0 and keys_pressed[K_LEFT]:
            self.rect.move_ip(-4, 0)

        if self.rect.right < SCREEN_WIDTH and keys_pressed[K_RIGHT]:
            self.rect.move_ip(4, 0)

        
    
player = Player()

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

        if event.type == KEYDOWN and event.key == K_ESCAPE:
            run = False

    player.update(pygame.key.get_pressed())


    screen.fill((0, 0, 50))
    screen.blit(player.surf, player.rect)
    
    pygame.display.flip()

    
pygame.quit()