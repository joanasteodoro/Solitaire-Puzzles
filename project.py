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
#slot called board that represents its state
class sol_state:
    def __init__(self, board):
        if(isinstance(board, list)):
            self.board = board
        else:
            self.marbles = board

    def __lt__(self, other_sol_state):
        return self.board < other_sol_state.board


class solitaire(Problem):
    def __init__(self, board):
        goal_number_marbles = 1 #nsei se podemos fazer isto porque quando chamamos a sol_state ela recebe um board e nao um inteiro
        self.board = board
        super(solitaire, self).__init__(sol_state(board), sol_state(goal_number_marbles))

    def actions(self, state):
        result = board_moves(state.board)
        return result

    def result(self, state, action):
        new_state = sol_state(board_perform_move(state.board, action))
        return new_state

    def goal_test(self, state):
        count = 0
        for i in range(len(state.board)):
            for j in range(len(state.board[i])):
                if(state.board[i][j] == "O"):
                    count += 1
        if(count != 1):
            return False
        return True

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def h(self, node):
        return 0
