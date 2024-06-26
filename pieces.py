import helpers
import pygame

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

    def render(self, screen):
        color = (0, 255, 255)
        pygame.draw.rect(screen, color, (self.x * helpers.boardSpaceSize, self.y * helpers.boardSpaceSize, helpers.boardSpaceSize, helpers.boardSpaceSize))

    def getVisibleTiles(self, pieces):
        chessboard = [[None for _ in range(8)] for _ in range(8)]
        # horizontal
        for i in range(8):
            for piece in pieces:
                if piece.x != i and piece.y != self.y:
                    chessboard[i][self.y] = True
        # vertical
        for i in range(8):
            for piece in pieces:
                if piece.x != self.x and piece.y != i:
                    chessboard[self.x][i] = True
        
        return chessboard


class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def move(self, level, x, y):

        print("not done")

    def render(self, screen):
        color = (0, 255, 255)
        pygame.draw.rect(screen, color, (self.x * helpers.boardSpaceSize, self.y * helpers.boardSpaceSize, helpers.boardSpaceSize, helpers.boardSpaceSize))

class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def move(self, level, x, y):

        print("not done")

    def render(self, screen):
        color = (0, 255, 255)
        pygame.draw.rect(screen, color, (self.x * helpers.boardSpaceSize, self.y * helpers.boardSpaceSize, helpers.boardSpaceSize, helpers.boardSpaceSize))

class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def move(self, level, x, y):

        print("not done")

    def render(self, screen):
        color = (0, 255, 255)
        pygame.draw.rect(screen, color, (self.x * helpers.boardSpaceSize, self.y * helpers.boardSpaceSize, helpers.boardSpaceSize, helpers.boardSpaceSize))

class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def move(self, level, x, y):

        print("not done")

    def render(self, screen):
        color = (0, 255, 255)
        pygame.draw.rect(screen, color, (self.x * helpers.boardSpaceSize, self.y * helpers.boardSpaceSize, helpers.boardSpaceSize, helpers.boardSpaceSize))