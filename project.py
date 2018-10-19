'''Artificial Intelligence's project
         - Solitaire Puzzles -
                            Group 24'''

from search import *
from utils import *


# -------- auxiliar functions --------
#TAI content
def c_peg():
    return "O"

def c_empty():
    return "_"

def c_blocked():
    return "X"

def is_empty(e):
    return e == c_empty()

def is_peg(e):
    return e == c_peg()

def is_blocked(e):
    return e == c_blocked()

#TAI pos
#Tuple (l, c)
def make_pos(l, c):
    return (l, c)

def pos_l(pos):
    return pos[0]

def pos_c(pos):
    return pos[1]

#TAI move
#List [p_initial, p_final]
def make_move(i, f):
    return [i, f]

def move_initial(move):
    return move[0]

def move_final(move):
    return move[1]

#TAI board
#List of lists that represent the game board's lines
#A sublist has a representation of a line's content
#which can be one and only one of Content type.
def board_moves(board):
    boardMoves = Problem(board)
    return boardMoves.actions(board)

def board_perform_move(board, move):
    return 0

def print_board(board):
    for l in board:
        print(l)
    return 0

#TAI sol_state
#
class sol_state:
    def __int__(self, board):
        self.board = board

    def __lt__(self, other_sol_state):
        return 0

# -------- main function --------
def main():
    board = [["_","O","O","O","_"], ["O","_","O","_","O"], ["_","O","_","O","_"], ["O","_","O","_","_"], ["_","O","_","_","_"]]
    print(board_moves(board))
    print_board(board)
    return 0


main()
