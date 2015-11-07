import pygame

class Worm:
    color = (255,255,255)
    
    def __init__(self):
        self.x = 0
        self.y = 0

    def draw(screen):
        pygame.draw.circle(screen, color, (self.x, self.y), 5)
        
        
        
