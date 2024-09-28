import pygameimporttime
import sys

# Initialize Pygame
game.init()

# Set up some constants
WIDTH,IGHT = 80, 800
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animation
IMAGES = {}

# Initialize a dictionary of images
def loadImages():
    pieces = ['wp', 'bp', 'wR', 'bR', 'wN', 'bN', 'wB', 'bB', 'wQ', 'bQ', 'wK', 'bK']
    for piece in pieces:
        IMAGES[piece] = pygame.image.load('images/' + piece + '.png')

# Returns a list of all valid moves for a given piece
def getAllPossibleMoves(piece, board):
    moves = []
    if piece.type == 'p':
        if piece.team == 'w':
            moves = getWhitePawnMoves(piece, board)
        else:
            moves = getBlackPawnMoves(piece, board)
    elif piece.type == 'R':
        moves = getRookMoves(piece, board)
    elif piece.type == 'N':
        moves = getKnightMoves(piece, board)
    elif piece.type == 'B':
        moves = getBishopMoves(piece, board)
    elif piece.type == 'Q':
        moves = getQueenMoves(piece, board)
    elif piece.type == 'K':
        moves = getKingMoves(piece, board)
    return moves

# Determine all possible squares a knight can move to
def getKnightMoves(piece, board):
    moves = []
    # Add all possible knight moves
    for r in range(1, 3):
        for c in range(1, 3):
            if r + piece.row < 8 and c + piece.col < 8:
                if (board[r + piece.row][c + piece.col] == '  ' or
                        board[r + piece.row][c + piece.col][0] != piece.team):
                    moves.append((r + piece.row, c + piece.col))
    return moves

# Determine all possible squares a bishop can move to
def getBishopMoves(piece, board):
    moves = []
    # Add all possible bishop moves
    for i in range(1, 8):
        if piece.row + i < 8 and piece.col + i < 8:
            if board[piece.row + i][piece.col + i] == '  ':
                moves.append((piece.row + i, piece.col + i))
            elif board[piece.row + i][piece.col + i][0] != piece.team:
                moves.append((piece.row + i, piece.col + i))
                break
        if piece.row - i >= 0 and piece.col + i < 8:
            if board[piece.row - i][piece.col + i] == '  ':
                moves.append((piece.row - i, piece.col + i))
            elif board[piece.row - i][piece.col + i][0] != piece.team:
                moves.append((piece.row - i, piece.col + i))
                break
        if piece.row + i < 8 and piece.col - i >= 0:
            if board[piece.row + i][piece.col - i] == '  ':
                moves.append((piece.row + i, piece.col - i))
            elif board[piece.row + i][piece.col - i][0] != piece.team:
                moves.append((piece.row + i, piece.col - i))
                break
        if piece.row - i >= 0 and piece.col - i >= 0:
            if board[piece.row - i][piece.col - i] == '  ':
                moves.append((piece.row - i, piece.col - i))
            elif board[piece.row - i][piece.col - i][0] != piece.team:
                moves.append((piece.row - i, piece.col - i))
                break
    return moves

# Determine all possible squares a rook can move to
def getRookMoves(piece, board):
    moves = []
    # Add all possible rook moves
    for i in range(1, 8):
        if piece.row + i < 8:
            if board[piece.row + i][piece.col] == '  ':
                moves.append((piece.row + i, piece.col))
            elif board[piece.row + i][piece.col][0] != piece.team:
                moves.append((piece.row + i, piece.col))
                break
        if piece.row - i >= 0:
            if board[piece.row - i][piece.col] == '  ':
                moves.append((piece.row - i, piece.col))
            elif board[piece.row - i][piece.col][0] != piece.team:
                moves.append((piece.row - i, piece.col))
                break
        if piece.col + i < 8:
            if board[piece.row][piece.col + i] == '  ':
                moves.append((piece.row, piece.col + i))
            elif board[piece.row][piece.col + i][0] != piece.team:
                moves.append((piece.row, piece.col + i))
                break
        if piece.col - i >= 0:
            if board[piece.row][piece.col - i] == '  ':
                moves.append((piece.row, piece.col - i))
            elif board[piece.row][piece.col - i][0] != piece.team:
                moves.append((piece.row, piece.col - i))
                break
    return moves

# Determine all possible squares a queen can move to
def getQueenMoves(piece, board):
    moves = getRookMoves(piece, board)
   