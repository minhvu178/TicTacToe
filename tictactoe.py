"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_turn = 0
    o_turn = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_turn += 1
            elif board[i][j] == O:
                o_turn += 1
    if x_turn == 0 and o_turn == 0:
        return X
    elif x_turn > o_turn:
        return O
    elif x_turn == o_turn:
        return X
    return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    acts = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                acts.add((i,j))
    return acts

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_cp=copy.deepcopy(board)
    turn=player(board_cp)
    x = action[0]
    y = action[1]
    if board_cp[x][y] != None:
        raise ActionInvalidError
    board_cp[x][y] = turn

    return board_cp

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for turn in [X,O]:
        for i in range(3):
            if board[i] == [turn, turn, turn]:
                return turn
            if board[0][i] == turn and board[1][i] == turn and board[2][i] == turn:
                return turn
        if  board[0][0] == turn and board[1][1] == turn and board[2][2] == turn:
            return turn
        if board[0][2] == turn and board[1][1] == turn and board[2][0] == turn:
            return turn
    return None
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    moves = 0
    for row in board:
        for turn in row:
            if turn == X or turn == O:
                moves += 1
    if moves == 9:
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0

def min_value(board):
    if terminal(board):
        return utility(board), None
    v = 100
    optimal = ()
    for action in actions(board):
        util, move = max_value(result(board, action))
        if util < v:
            v = util
            optimal = action
            if v == -1:
                return v, optimal

    return v, optimal

def max_value(board):
    if terminal(board):
        return utility(board), None
    v = -100
    optimal = ()
    for action in actions(board):
        util, move = min_value(result(board, action))
        if util > v:
            v = util
            optimal = action
            if v == 1:
                return v, optimal

    return v, optimal

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board)==X:
        value, move = max_value(board)
        return move
    if player(board)==O:
        value, move = min_value(board)
        return move
