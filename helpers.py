import helpers

boardSpaceSize = 480 / 8

def is_in_bounds(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def checkLineTile(directions, x, y, color, pieces):
    chessboard = [[None for _ in range(8)] for _ in range(8)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        while helpers.is_in_bounds(nx, ny):
            piece = next((piece for piece in pieces if piece.x == nx and piece.y == ny), None)
            if piece:
                # check if tile is capturable
                chessboard[nx][ny] = piece.color != color
                break
            chessboard[nx][ny] = True
            nx += dx
            ny += dy

    return chessboard
