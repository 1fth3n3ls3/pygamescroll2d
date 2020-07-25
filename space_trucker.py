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
ENEMY_COUNT = 20



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

class Enemy(pygame.sprite.DirtySprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((16, 4))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center = self._get_random_pos())
        self.speed = random.randint(4, 16)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0: self.kill()

    def spawn(self):
        self.rect.center = self._get_random_pos()
    def _get_random_pos(self):
        return random.randint(SCREEN_WIDTH + 16, SCREEN_WIDTH + 128), random.randint(0, SCREEN_HEIGHT)


def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ADDENEMY = pygame.USEREVENT + 1 # create new userevent
    pygame.time.set_timer(ADDENEMY, 250)

    run = True        
    enemy_counter = 0    
    player = Player()


    enemies = pygame.sprite.Group()
    enemies_pool = [Enemy() for i in range(ENEMY_COUNT)]

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)


    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                run = False

            if event.type == ADDENEMY:
                enemy_counter = 0 if enemy_counter >= ENEMY_COUNT-1 else enemy_counter + 1
                enemy = enemies_pool[enemy_counter]
                if not enemy.alive():
                    enemy.spawn()
                    enemies.add(enemy)
                    all_sprites.add(enemy)

            if pygame.sprite.spritecollideany(player, enemies):
                player.kill()
                run = False

        player.update(pygame.key.get_pressed())

        enemies.update()


        screen.fill((0, 0, 50))
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        pygame.display.flip()
        clock.tick(60)
    
    



if __name__ == "__main__":
    pygame.init()
    import cProfile as profile
    profile.run("main()")
    # main()  
    pygame.quit()
