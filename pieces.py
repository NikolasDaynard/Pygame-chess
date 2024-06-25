import pygame

class Rook:
    def __init__(self, color, x, y):
        self.color = color  # Initialize the color attribute
        self.x = x
        self.y = y

    def move(self, level, x, y):
        
        print("not done")

    def render(self, screen):
        color = (0, 255, 255)
        pygame.draw.rect(screen, color, (self.x * 20, self.y * 20, 20, 20))