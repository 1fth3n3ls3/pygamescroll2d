import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

run = True

screen.fill((255, 255, 0))
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.draw.circle(screen, (255, 0, 255), (320, 240), 64)
    pygame.display.flip()

    
pygame.quit()