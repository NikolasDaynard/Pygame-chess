import pygame

def drawBoard(screen):
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = (255, 255, 255)  # White
            else:
                color = (0, 0, 0)  # Black
            pygame.draw.rect(screen, color, (i * 20, j * 20, 20, 20))