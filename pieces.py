import helpers
import pygame
import helpers

class Piece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def move(self, level, x, y):

        print("not done")

    def render(self, screen, imagerenderer):
        imagerenderer.renderImage(screen, 'aesprites/rookwhite.png', self.x * helpers.boardSpaceSize, self.y * helpers.boardSpaceSize, helpers.boardSpaceSize, helpers.boardSpaceSize)

    def getVisibleTiles(self, pieces):
        directions = [
                    (1, 0), (-1, 0),  # Horizontal
                    (0, 1), (0, -1),  # Vertical
                ]
        
        return helpers.checkLineTile(directions, self.x, self.y, pieces)


class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def move(self, level, x, y):

        print("not done")

    def render(self, screen, imagerenderer):
        color = (0, 255, 255)
        pygame.draw.rect(screen, color, (self.x * helpers.boardSpaceSize, self.y * helpers.boardSpaceSize, helpers.boardSpaceSize, helpers.boardSpaceSize))

    def getVisibleTiles(self, pieces):
        chessboard = [[None for _ in range(8)] for _ in range(8)]

        accessibleTileOffsets = [(-1, 2), (1, 2), (2, 1), (2, -1),
                                 (-1, -2), (1, -2), (-2, 1), (-2, -1)
                                ]

        for offset in accessibleTileOffsets:
            for piece in pieces:
                if helpers.is_in_bounds(self.x + offset[0], self.y + offset[1]):
                    if not(piece.x == self.x + offset[0] and piece.y == self.y + offset[1]):
                        if chessboard[self.x + offset[0]][self.y + offset[1]] != False:
                            chessboard[self.x + offset[0]][self.y + offset[1]] = True
                    else:
                        chessboard[self.x + offset[0]][self.y + offset[1]] = False
        
        return chessboard

class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def move(self, level, x, y):

        print("not done")

    def render(self, screen, imagerenderer):
        color = (0, 255, 255)
        pygame.draw.rect(screen, color, (self.x * helpers.boardSpaceSize, self.y * helpers.boardSpaceSize, helpers.boardSpaceSize, helpers.boardSpaceSize))
    def getVisibleTiles(self, pieces):
        directions = [
                    (1, 1), (-1, -1), (1, -1), (-1, 1)  # Diagonal
                ]
        
        return helpers.checkLineTile(directions, self.x, self.y, pieces)

class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def move(self, level, x, y):

        print("not done")

    def render(self, screen, imagerenderer):
        color = (0, 255, 255)
        pygame.draw.rect(screen, color, (self.x * helpers.boardSpaceSize, self.y * helpers.boardSpaceSize, helpers.boardSpaceSize, helpers.boardSpaceSize))

    def getVisibleTiles(self, pieces):
        directions = [
                    (1, 0), (-1, 0),  # Horizontal
                    (0, 1), (0, -1),  # Vertical
                    (1, 1), (-1, -1), (1, -1), (-1, 1)  # Diagonal
                ]
        
        return helpers.checkLineTile(directions, self.x, self.y, pieces)

class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def move(self, level, x, y):

        print("not done")

    def render(self, screen, imagerenderer):
        color = (0, 255, 255)
        pygame.draw.rect(screen, color, (self.x * helpers.boardSpaceSize, self.y * helpers.boardSpaceSize, helpers.boardSpaceSize, helpers.boardSpaceSize))

    def getVisibleTiles(self, pieces):
        chessboard = [[None for _ in range(8)] for _ in range(8)]

        # not gonna pretend these are ordered
        accessibleTileOffsets = [(1, 0), (-1, 0), (1, 1), (-1, -1), 
                                (0, 1), (0, -1), (1, -1), (-1, 1)
                                ]

        for offset in accessibleTileOffsets:
            for piece in pieces:
                if helpers.is_in_bounds(self.x + offset[0], self.y + offset[1]):
                    if not(piece.x == self.x + offset[0] and piece.y == self.y + offset[1]):
                        if chessboard[self.x + offset[0]][self.y + offset[1]] != False:
                            chessboard[self.x + offset[0]][self.y + offset[1]] = True
                    else:
                        chessboard[self.x + offset[0]][self.y + offset[1]] = False
        
        return chessboard
    
class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def move(self, level, x, y):

        print("not done")

    def render(self, screen, imagerenderer):
        imagerenderer.renderImage(screen, 'aesprites/whitepawn.png', self.x * helpers.boardSpaceSize, self.y * helpers.boardSpaceSize, helpers.boardSpaceSize, helpers.boardSpaceSize)

    def getVisibleTiles(self, pieces):
        chessboard = [[None for _ in range(8)] for _ in range(8)]

        # not gonna pretend these are ordered
        accessibleTileOffsets = [(1, 0), (-1, 0), (1, 1), (-1, -1), 
                                (0, 1), (0, -1), (1, -1), (-1, 1)
                                ]

        for offset in accessibleTileOffsets:
            for piece in pieces:
                if helpers.is_in_bounds(self.x + offset[0], self.y + offset[1]):
                    if not(piece.x == self.x + offset[0] and piece.y == self.y + offset[1]):
                        if chessboard[self.x + offset[0]][self.y + offset[1]] != False:
                            chessboard[self.x + offset[0]][self.y + offset[1]] = True
                    else:
                        chessboard[self.x + offset[0]][self.y + offset[1]] = False
        
        return chessboard