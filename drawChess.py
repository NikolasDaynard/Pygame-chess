import random
import pygame
from images import imageRenderer
import pieces
import helpers

class chessBoard:
    playPieces = [
                pieces.Rook("black", 0, 0), pieces.Knight("black", 1, 0), pieces.Bishop("black", 2, 0), pieces.Queen("black", 3, 0), pieces.King("black", 4, 0), pieces.Bishop("black", 5, 0), pieces.Knight("black", 6, 0), pieces.Rook("black", 7, 0),
                pieces.Pawn("black", 0, 1), pieces.Pawn("black", 1, 1), pieces.Pawn("black", 2, 1), pieces.Pawn("black", 3, 1), pieces.Pawn("black", 4, 1), pieces.Pawn("black", 5, 1), pieces.Pawn("black", 6, 1), pieces.Pawn("black", 7, 1),
                pieces.Rook("white", 0, 7), pieces.Knight("white", 1, 7), pieces.Bishop("white", 2, 7), pieces.Queen("white", 3, 7), pieces.King("white", 4, 7), pieces.Bishop("white", 5, 7), pieces.Knight("white", 6, 7), pieces.Rook("white", 7, 7),
                pieces.Pawn("white", 0, 6), pieces.Pawn("white", 1, 6), pieces.Pawn("white", 2, 6), pieces.Pawn("white", 3, 6), pieces.Pawn("white", 4, 6), pieces.Pawn("white", 5, 6), pieces.Pawn("white", 6, 6), pieces.Pawn("white", 7, 6)
                ]

    selectedSpace = (-1, -1)

    image = imageRenderer()

    def click(self, x, y, color):
        clickedPiece = False
        selectedPiece = None
        moved = False

        for piece in self.playPieces:
            if piece.x == self.selectedSpace[0] and piece.y == self.selectedSpace[1]:
                selectedPiece = piece

        if selectedPiece != None:
            visibleTiles = selectedPiece.getVisibleTiles(self.playPieces)
        else:
            visibleTiles = [[None for _ in range(8)] for _ in range(8)]

        
        
        for piece in self.playPieces:
            if (piece.x * helpers.boardSpaceSize) < x and (piece.x * helpers.boardSpaceSize) + helpers.boardSpaceSize > x and (piece.y * helpers.boardSpaceSize) < y and (piece.y * helpers.boardSpaceSize) + helpers.boardSpaceSize > y:
                if piece.color == color:
                    self.selectedSpace = (piece.x, piece.y)

                if visibleTiles[piece.x][piece.y] != None and piece.color != color:
                    self.playPieces.remove(piece)

                    selectedPiece.x = piece.x
                    selectedPiece.y = piece.y
                    self.selectedSpace = (-1, -1)
                    moved = True
                    break

                clickedPiece = True

        if not clickedPiece:
            for i in range(8):
                for j in range(8):
                    if visibleTiles[i][j] == True:
                        if (i * helpers.boardSpaceSize) < x and (i * helpers.boardSpaceSize) + helpers.boardSpaceSize > x and (j * helpers.boardSpaceSize) < y and (j * helpers.boardSpaceSize) + helpers.boardSpaceSize > y:
                            visibleTiles[i][j] = None
                            selectedPiece.x = i
                            selectedPiece.y = j
                            moved = True
            self.selectedSpace = (-1, -1)
        return moved

                    


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
                            self.image.renderImage(screen, 'aesprites/clicker.png', i * helpers.boardSpaceSize, j * helpers.boardSpaceSize, helpers.boardSpaceSize, helpers.boardSpaceSize)