import pygame

class Worm:
 
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255,255,255)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 5)
        
        
        
