import pygame
from images import imageRenderer
import pieces
import helpers

class chessBoard:
    playPieces = [
                pieces.Rook("black", 0, 0), pieces.Knight("black", 1, 0), pieces.Bishop("black", 2, 0), pieces.Queen("black", 3, 0), pieces.King("black", 4, 0), pieces.Bishop("black", 5, 0), pieces.Knight("black", 6, 0), pieces.Rook("black", 7, 0),
                pieces.Pawn("black", 0, 1), pieces.Pawn("black", 1, 1), pieces.Pawn("black", 2, 1), pieces.Pawn("black", 3, 1), pieces.Pawn("black", 4, 1), pieces.Pawn("black", 5, 1), pieces.Pawn("black", 6, 1), pieces.Pawn("black", 7, 1)
                ]

    selectedSpace = (-1, -1)

    image = imageRenderer()

    def click(self, x, y):
        clickedPiece = False
        for piece in self.playPieces:
            if (piece.x * helpers.boardSpaceSize) < x and (piece.x * helpers.boardSpaceSize) + helpers.boardSpaceSize > x and (piece.y * helpers.boardSpaceSize) < y and (piece.y * helpers.boardSpaceSize) + helpers.boardSpaceSize > y:
                self.selectedSpace = (piece.x, piece.y)
                clickedPiece = True

        if not clickedPiece:
            for piece in self.playPieces:
                if piece.x == self.selectedSpace[0] and piece.y == self.selectedSpace[1]:
                    visibleTiles = piece.getVisibleTiles(self.playPieces)
                    for i in range(8):
                        for j in range(8):
                            if visibleTiles[i][j] == True:
                                if (i * helpers.boardSpaceSize) < x and (i * helpers.boardSpaceSize) + helpers.boardSpaceSize > x and (j * helpers.boardSpaceSize) < y and (j * helpers.boardSpaceSize) + helpers.boardSpaceSize > y:
                                    piece.x = i
                                    piece.y = j

                    


    def drawBoard(self, screen):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = (255, 255, 255)  # White
                else:
                    color = (0, 0, 0)  # Black
                pygame.draw.rect(screen, color, (i * helpers.boardSpaceSize, j * helpers.boardSpaceSize, helpers.boardSpaceSize, helpers.boardSpaceSize))

        for piece in self.playPieces:
            piece.render(screen, self.image)
            if piece.x == self.selectedSpace[0] and piece.y == self.selectedSpace[1]:
                visibleTiles = piece.getVisibleTiles(self.playPieces)
                for i in range(8):
                    for j in range(8):
                        if visibleTiles[i][j] == True:
                            pygame.draw.rect(screen, (127, 127, 127), (i * helpers.boardSpaceSize, j * helpers.boardSpaceSize, helpers.boardSpaceSize / 2, helpers.boardSpaceSize / 2))