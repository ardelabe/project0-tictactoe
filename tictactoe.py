"""
Tic Tac Toe Player
"""

import copy


# variables to represent possible moves of the board
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0

    # iterate over board counting
    for row in board:
        for value in row: 
            if value == X: 
                count_x += 1
            if value == O:
                count_o += 1
            
    # checking results
    board_marks = count_x + count_o
    if board_marks == 9:
        return "the game is already over"
    elif (board_marks % 2) == 0:
        return X
    else: 
        return O   


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the 
    board.
    """
    actions_set = set()

    # iterate over board adding empty slots to actions_set
    for row in enumerate(board):
        for value in enumerate(row[1]):
            if value[1] == EMPTY:
                empty_slot = (row[0], value[0])
                actions_set.add(empty_slot)
    
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the 
    board.
    """
    # taking a deepcopy to not mess with the original board
    copied_board = copy.deepcopy(board)

    # takes the board and checks whose turn it is
    value_to_assing = player(copied_board)

    # iterates to place the value (if is EMPTY)
    if (copied_board[action[0]][action[1]]) is not EMPTY:
        raise NameError("Invalid Action")
    else:
        copied_board[action[0]][action[1]] = value_to_assing

    return copied_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    first_column = []
    second_column = []
    third_column = []
    back_diagonal = []
    forward_diagonal = []
    
    results = [
        first_column, 
        second_column, 
        third_column,
        back_diagonal, 
        forward_diagonal,
    ]

    iteration_counter = 0
    
    # check rows for winner
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
        
        # list column values
        first_column.append(row[0])
        second_column.append(row[1])
        third_column.append(row[2])
        
        # list diagonal values
        back_diagonal.append(row[iteration_counter])
        forward_diagonal.append(row[2 - iteration_counter])

        iteration_counter += 1

    # check results
    for i in results:
        if len(set(i)) == 1 and i[0] is not None:
            return i[0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # there is winner, return True
    if winner(board) is not None:
        return True

    # there is EMPTY cells, return False
    for row in board:
        for value in row:
            if value == EMPTY:
                return False

    # there is no winner, but no EMPTY cells
    return True


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
    v = -2
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    v = 2
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """ 
    Returns the optimal action for the current player on the board.
    """
    action_value = {}
    if player(board) == X:
        for action in actions(board):
            board_to_evaluate = result(board, action)
            action_value[action] = min_value(board_to_evaluate)
        print(max(action_value, key=action_value.get))
        return max(action_value, key=action_value.get)
    else:
        for action in actions(board):
            board_to_evaluate = result(board, action)
            # action_value[action] = max_value(board_to_evaluate)
            action_value[action] = max_value(board_to_evaluate)
        return min(action_value, key=action_value.get)