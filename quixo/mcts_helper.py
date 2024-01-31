import random
import numpy as np
from game import Move

SIDES = [(1,0), (2,0), (3,0), (4,0),
         (1,4), (2,4), (3,4), (4,4),
         (0,1), (0,2), (0,3), (0,4),
         (4,1), (4,2), (4,3), (0,0)]

MOVES = [Move.TOP,
         Move.LEFT,
         Move.BOTTOM,
         Move.RIGHT]

def get_legal_moves(board: np.ndarray, player_id: int):   
    legal_moves = []

    for x, y in SIDES:
        if board[y,x] == player_id or board[y,x] == -1:
            moves = MOVES.copy()
            if x == 4:
                moves.remove(Move.RIGHT)
            if x == 0:
                moves.remove(Move.LEFT)
            if y == 4:
                moves.remove(Move.BOTTOM)
            if y == 0:
                moves.remove(Move.TOP)

            legal_moves.extend([((x,y), m) for m in moves])

    random.shuffle(legal_moves)
    
    return legal_moves