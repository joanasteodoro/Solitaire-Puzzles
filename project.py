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
    result = []
    l = len(board)
    for i in range(l):
        c = len(board[i])
        for j in range(c):
            if(board[i][j] == "O"):
                if(j-2 >= 0 and board[i][j-2] == "_" and board[i][j-1] == "O"):
                    result += [[(i, j), (i, j-2)]]
                if(j+2 < c and board[i][j+2] == "_" and board[i][j+1] == "O"):
                    result += [[(i, j), (i, j+2)]]
                if i+2 < l and board[i+2][j] == "_" and board[i+1][j] == "O":
                    result += [[(i, j), (i+2, j)]]
                if i-2 >= 0 and board[i-2][j] == "_" and board[i-1][j] == "O":
                    result += [[(i, j), (i-2, j)]]
    return result

def board_perform_move(board, move):
    if(move[0][0] == move[1][0] and move[0][1] - move[1][1] > 0):
        board[move[0][0]][move[0][1]-1] = "_"
    elif(move[0][0] == move[1][0] and move[0][0]):
        board[move[0][0]][move[0][1]+1] = "_"
    elif(move[0][1] == move[1][1] and move[0][0] - move[1][0] > 0):
        board[move[0][0]-1][move[0][1]] = "_"
    else:
        board[move[0][0]+1][move[0][1]] = "_"

    board[move[0][0]][move[0][1]] = "_"
    board[move[1][0]][move[1][1]] = "O"
    return board

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
    print("____________________________" + "\n")
    print_board(board_perform_move(board, [(0, 2), (0, 0)]))
    return 0


main()
