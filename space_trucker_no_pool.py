import pygame
import random

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

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((16, 4))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center = (random.randint(SCREEN_WIDTH + 16, SCREEN_WIDTH + 128),
                      random.randint(0, SCREEN_HEIGHT))
        )
        self.speed = random.randint(4, 32)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0: self.kill()

def main():       


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ADDENEMY = pygame.USEREVENT + 1 # create new userevent
    pygame.time.set_timer(ADDENEMY, 250)

    run = True

    player = Player()

    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                run = False

            if event.type == ADDENEMY:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        player.update(pygame.key.get_pressed())

        enemies.update()


        screen.fill((0, 0, 50))
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        pygame.display.flip()

        

if __name__ == "__main__":
    import cProfile as profile
    # main()
    pygame.init()

    profile.run("main()")
    pygame.quit()
