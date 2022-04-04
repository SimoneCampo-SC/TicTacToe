"""
Tic Tac Toe Player
"""
import copy
import math

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
    count_x = 0
    count_O = 0

    for row in board:
        for player in row:
            if player == X:
                count_x += 1
            elif player == O:
                count_O += 1

    if count_x == count_O:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    
    row_count = 0
    col_count = 0
    for row in board:
        row_count += 1
        col_count = 0
        for player in row:
            col_count += 1
            if player == None:
                possible_actions.add((row_count - 1, col_count - 1))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    try:
        copyboard = copy.deepcopy(board)
        row = copyboard[action[0]]

        if row[action[1]] == None:
            row[action[1]] = player(board)
    except NameError:
        print("error")

    return copyboard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check Horizzontally
    for row in board:
        if len(set(row)) == 1 and row[0] != None:
            return row[0]
    
    # Check Vertically
    for j in range(3):
        if len(set([board[i][j] for i in range(len(board))])) == 1 and board[0][j] != None:
            return board[0][j]
    
    # Check Diagonally 
    if len(set([board[i][i] for i in range(len(board))])) == 1 and board[0][0] != None:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1 and board[0][len(board)-1] != None:
        return board[0][len(board)-1]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if len(actions(board)) == 0 or winner(board) != None:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """ 
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v 

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        list = []
        for action in actions(board):
            list.append([min_value(result(board, action)), action])
        return sorted(list, key=lambda x: x[0], reverse=True)[0][1]
    elif player(board) == O:
        list = []
        for action in actions(board):
            list.append([max_value(result(board, action)), action])
        return sorted(list, key=lambda x: x[0])[0][1]