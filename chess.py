import random
import pygame, sys
import drawChess
import pieces
import helpers

pygame.init()

screen = pygame.display.set_mode((640, 480))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# image = pygame.image.load('aesprites/whitepawn.png')


board = drawChess.chessBoard()

clock = pygame.time.Clock()

currentTurn = "white"

playAi = True

def render():
    board.drawBoard(screen)

pygame.display.set_caption("Hello World")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            pygame.quit()
            sys.exit()
        if ((event.type == pygame.MOUSEBUTTONDOWN) and (event.button == pygame.BUTTON_LEFT)) or (currentTurn == "black" and playAi):
            if playAi and currentTurn == "black":
                x, y = 0, 0
                if currentTurn == "black":
                    if board.selectedSpace[0] == -1:
                        for piece in board.playPieces:
                            if random.randint(0, 10) == 9:
                                x = piece.x * helpers.boardSpaceSize + 3
                                y = piece.y * helpers.boardSpaceSize + 3
                    else:
                        x = random.randint(0, 480)
                        y = random.randint(0, 480)
            else:
                x, y = pygame.mouse.get_pos()

            if board.click(x, y, currentTurn):
                if currentTurn == "white":
                    currentTurn = "black"
                else:
                    currentTurn = "white"

    screen.fill((0, 0, 0))  # Fill with black to clear previous drawings

    render()

    pygame.display.flip()

    clock.tick(60)




