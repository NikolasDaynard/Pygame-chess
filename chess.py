import pygame, sys
import drawChess
pygame.init()

screen = pygame.display.set_mode((640, 480))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

WhitePawn = 1
WhiteRook = 2
WhiteBishop = 2
WhiteRook = 2
WhiteRook = 2

chessBoard = [8, 8]

def render():
    drawChess.drawBoard(screen)

pygame.display.set_caption("Hello World")
while True:
   for event in pygame.event.get():
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
        pygame.quit()
        sys.exit()
    if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == pygame.BUTTON_LEFT):
       print("lmp")

    screen.fill((0, 0, 0))  # Fill with black to clear previous drawings

    render()

    pygame.display.flip()




