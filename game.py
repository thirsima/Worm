from worm import Worm
import pygame

worms = [Worm(100, 100), Worm(900, 400)]
screen_size = (1000, 500)

pygame.init()
screen = pygame.display.set_mode(screen_size)
    
        
while True:
    
    for worm in worms:
        worm.draw(screen)
    pygame.display.update()


    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            break


pygame.quit()
