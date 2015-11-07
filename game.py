from worm import Worm
import pygame

screen_size = (1000, 500)

# create worms
worms = [Worm(100, 100), Worm(900, 400)]

# create screen
pygame.init()
screen = pygame.display.set_mode(screen_size)

# create timer 
timer_event = pygame.USEREVENT
pygame.time.set_timer(timer_event, 250)
        
while True:

    event = pygame.event.wait()

    if event.type == timer_event:        
        for worm in worms:
            worm.move()
            worm.draw(screen)
        pygame.display.update()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            break

pygame.quit()
