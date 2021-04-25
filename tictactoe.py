"""
Tic Tac Toe Player
"""

from math import inf
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

currentPlayerOtherPlayerMap = {
    'X': 'O',
    'O': 'X'
}


def initial_state():
    # Returns starting state of the localBoard.
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(localBoard):
    # Returns player who has the next turn on a localBoard.
    countX = 0
    countO = 0

    for i in range(3):
        for j in range(3):
            if 'X' == localBoard[i][j]:
                countX += 1
            if 'O' == localBoard[i][j]:
                countO += 1

    if countX > countO:
        return 'O'
    else:
        return 'X'


def actions(localBoard):
    # Returns set of all possible actions (i, j) available on the localBoard.
    availableSquares = set()
    for i in range(3):
        for j in range(3):
            if localBoard[i][j] == EMPTY:
                availableSquares.add((i, j))
    return availableSquares


def minimax(localBoard):
    # Returns the optimal action for the current player on the localBoard.
    if terminal(localBoard):
        return None

    currentPlayer = player(localBoard)

    # if X, we maximize
    if currentPlayer == 'X':
        v, bestMove = maxValue(localBoard)

    # if O, we minimize
    if currentPlayer == 'O':
        v,bestMove = minValue(localBoard)
    return bestMove



def maxValue(localBoard):
    # Returns the max value possible (do we need to include action?
    if terminal(localBoard):
        return utility(localBoard), tuple()

    v = -inf
    bestMove = tuple()

    for rowCol in list(actions(localBoard)):
        potentialBoard = result(localBoard, rowCol)
        minV, potentialMove = minValue(potentialBoard)
        if minV > v:
            v = minV
            bestMove = rowCol
    return (v,bestMove)


def minValue(localBoard):
    """
    Returns the min value possible (do we need to include action?
    """
    if terminal(localBoard):
        return utility(localBoard), tuple()

    v = inf
    bestMove = tuple()

    for rowCol in list(actions(localBoard)):
        potentialBoard = result(localBoard, rowCol)
        maxV, potentialMove = maxValue(potentialBoard)
        if v > maxV:
            v = maxV
            bestMove = rowCol

    return (v,bestMove)


def result(currentBoard, action):
    # Returns the localBoard that results from making move (i, j) on the localBoard.
    newBoard = deepcopy(currentBoard)

    if terminal(newBoard):
        return newBoard

    (row, col) = action
    if newBoard[row][col] is not EMPTY:
        raise Exception("Space not available")

    newBoard[row][col] = player(newBoard)
    return newBoard


def terminal(localBoard):
    # Returns True if game is over, False otherwise.
    if hasWinningBoard(localBoard,'X'):
        return True
    if hasWinningBoard(localBoard,'O'):
        return True
    if not actions(localBoard):
        return True
    return False


def winner(localBoard):
    # Returns the winner of the game, if there is one.
    if hasWinningBoard(localBoard,'X'):
        return 'X'
    elif hasWinningBoard(localBoard,'O'):
        return 'O'
    else:
        return None


def utility(localBoard):
    # Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    if hasWinningBoard(localBoard, 'X'):
        return 1
    elif hasWinningBoard(localBoard, 'O'):
        return -1
    else:
        return 0


def hasWinningBoard(localBoard, currentPlayer):
    # Returns True if currentPlayer has a winning localBoard
    # rows
    if localBoard[0][0] == currentPlayer and localBoard[0][1] == currentPlayer and localBoard[0][2] == currentPlayer:
        return True
    if localBoard[1][0] == currentPlayer and localBoard[1][1] == currentPlayer and localBoard[1][2] == currentPlayer:
        return True
    if localBoard[2][0] == currentPlayer and localBoard[2][1] == currentPlayer and localBoard[2][2] == currentPlayer:
        return True
    # columns
    if localBoard[0][0] == currentPlayer and localBoard[1][0] == currentPlayer and localBoard[2][0] == currentPlayer:
        return True
    if localBoard[0][1] == currentPlayer and localBoard[1][1] == currentPlayer and localBoard[2][1] == currentPlayer:
        return True
    if localBoard[0][2] == currentPlayer and localBoard[1][2] == currentPlayer and localBoard[2][2] == currentPlayer:
        return True
    # diags
    if localBoard[0][0] == currentPlayer and localBoard[1][1] == currentPlayer and localBoard[2][2] == currentPlayer:
        return True
    if localBoard[0][2] == currentPlayer and localBoard[1][1] == currentPlayer and localBoard[2][0] == currentPlayer:
        return True
    return False
