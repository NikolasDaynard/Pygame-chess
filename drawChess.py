import pygame
import pieces

class chessBoard:
    boardSpaceSize = 480 / 8

    playPieces = [pieces.Rook("white", 1, 1)]

    selectedSpace = (-1, -1)

    def click(self, x, y):
        for piece in self.playPieces:
            piece.x

    def drawBoard(self, screen):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = (255, 255, 255)  # White
                else:
                    color = (0, 0, 0)  # Black
                pygame.draw.rect(screen, color, (i * 20, j * 20, 20, 20))

        for piece in self.playPieces:
            piece.render(screen)