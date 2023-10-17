import random

import game_rules

###########################################################################
# Explanation of the types:
# The board is represented by a row-major 2D list of characters, 0 indexed
# A point is a tuple of (int, int) representing (row, column)
# A move is a tuple of (point, point) representing (origin, destination)
# A jump is a move of length 2
###########################################################################

# I will treat these like constants even though they aren't
# Also, these values obviously are not real infinity, but close enough for
# this purpose
NEG_INF = -1000000000
POS_INF = 1000000000


class Player(object):
    """This is the player interface that is consumed by the GameManager."""

    def __init__(self, symbol):
        self.symbol = symbol  # 'x' or 'o'

    def __str__(self):
        return str(type(self))

    def selectInitialX(self, board):
        return (0, 0)

    def selectInitialO(self, board):
        pass

    def getMove(self, board):
        pass

    def h1(self, board):
        return -len(game_rules.getLegalMoves(board, "o" if self.symbol == "x" else "x"))

    def h2(self, board):
        """
        Account for player mobility and opponent mobility.
        """
        player_symbol = self.symbol
        opponent_symbol = "o" if player_symbol == "x" else "x"
        player_mobility = len(game_rules.getLegalMoves(board, player_symbol))
        opponent_mobility = len(game_rules.getLegalMoves(board, opponent_symbol))
        return player_mobility - opponent_mobility


# This class has been replaced with the code for a deterministic player.
class MinimaxPlayer(Player):
    def __init__(self, symbol, depth):
        super(MinimaxPlayer, self).__init__(symbol)
        self.depth = depth

    # Leave these two functions alone.
    def selectInitialX(self, board):
        return (0, 0)

    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    # Edit this one here. :)
    def getMove(self, board):
        best_move, _ = self._get_minimax_value(board, self.depth, self.symbol)
        return best_move

    def _get_minimax_value(self, board, depth, symbol):
        return self._get_max_value(board, depth, symbol)

    def _get_max_value(self, board, depth, symbol):
        legal_moves = game_rules.getLegalMoves(board, symbol)
        if depth == 0 or len(legal_moves) == 0:
            return None, self.h1(board)

        best_move = None
        best_value = NEG_INF
        for legal_move in legal_moves:
            board_after_next_move = game_rules.makeMove(board, legal_move)
            next_symbol = "o" if symbol == "x" else "x"
            _, next_value = self._get_min_value(
                board_after_next_move, depth - 1, next_symbol
            )
            if next_value > best_value:
                best_value = next_value
                best_move = legal_move

        return best_move, best_value

    def _get_min_value(self, board, depth, symbol):
        legal_moves = game_rules.getLegalMoves(board, symbol)
        if depth == 0 or len(legal_moves) == 0:
            return None, self.h1(board)

        best_move = None
        best_value = POS_INF
        for legal_move in legal_moves:
            board_after_next_move = game_rules.makeMove(board, legal_move)
            next_symbol = "o" if symbol == "x" else "x"
            _, next_value = self._get_max_value(
                board_after_next_move, depth - 1, next_symbol
            )
            if next_value < best_value:
                best_value = next_value
                best_move = legal_move

        return best_move, best_value


# This class has been replaced with the code for a deterministic player.
class AlphaBetaPlayer(Player):
    def __init__(self, symbol, depth):
        super(AlphaBetaPlayer, self).__init__(symbol)
        self.depth = depth

    # Leave these two functions alone.
    def selectInitialX(self, board):
        return (0, 0)

    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    # Edit this one here. :)
    def getMove(self, board):
        best_move, _ = self._get_minimax_value(board, self.depth, self.symbol)
        return best_move

    def _get_minimax_value(self, board, depth, symbol):
        alpha = NEG_INF
        beta = POS_INF
        return self._get_max_value(board, alpha, beta, depth, symbol)

    def _get_max_value(self, board, alpha, beta, depth, symbol):
        legal_moves = game_rules.getLegalMoves(board, symbol)
        if depth == 0 or len(legal_moves) == 0:
            return None, self.h1(board)

        best_move = None
        best_value = NEG_INF
        for legal_move in legal_moves:
            board_after_next_move = game_rules.makeMove(board, legal_move)
            next_symbol = "o" if symbol == "x" else "x"
            _, next_value = self._get_min_value(
                board_after_next_move, alpha, beta, depth - 1, next_symbol
            )
            if next_value > best_value:
                best_value = next_value
                best_move = legal_move
            if best_value >= beta:
                return best_move, best_value
            if next_value >= alpha:
                alpha = next_value
        return best_move, best_value

    def _get_min_value(self, board, alpha, beta, depth, symbol):
        legal_moves = game_rules.getLegalMoves(board, symbol)
        if depth == 0 or len(legal_moves) == 0:
            return None, self.h1(board)

        best_move = None
        best_value = POS_INF
        for legal_move in legal_moves:
            board_after_next_move = game_rules.makeMove(board, legal_move)
            next_symbol = "o" if symbol == "x" else "x"
            _, next_value = self._get_max_value(
                board_after_next_move, alpha, beta, depth - 1, next_symbol
            )
            if next_value < best_value:
                best_value = next_value
                best_move = legal_move
            if best_value <= alpha:
                return best_move, best_value
            if next_value <= beta:
                beta = next_value
        return best_move, best_value


class RandomPlayer(Player):
    def __init__(self, symbol):
        super(RandomPlayer, self).__init__(symbol)

    def selectInitialX(self, board):
        validMoves = game_rules.getFirstMovesForX(board)
        return random.choice(list(validMoves))

    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return random.choice(list(validMoves))

    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        if len(legalMoves) > 0:
            return random.choice(legalMoves)
        else:
            return None


class DeterministicPlayer(Player):
    def __init__(self, symbol):
        super(DeterministicPlayer, self).__init__(symbol)

    def selectInitialX(self, board):
        return (0, 0)

    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        if len(legalMoves) > 0:
            return legalMoves[0]
        else:
            return None


class HumanPlayer(Player):
    def __init__(self, symbol):
        super(HumanPlayer, self).__init__(symbol)

    def selectInitialX(self, board):
        raise NotImplementedException(
            "HumanPlayer functionality is handled externally."
        )

    def selectInitialO(self, board):
        raise NotImplementedException(
            "HumanPlayer functionality is handled externally."
        )

    def getMove(self, board):
        raise NotImplementedException(
            "HumanPlayer functionality is handled externally."
        )


def makePlayer(playerType, symbol, depth=1):
    player = playerType[0].lower()
    if player == "h":
        return HumanPlayer(symbol)
    elif player == "r":
        return RandomPlayer(symbol)
    elif player == "m":
        return MinimaxPlayer(symbol, depth)
    elif player == "a":
        return AlphaBetaPlayer(symbol, depth)
    elif player == "d":
        return DeterministicPlayer(symbol)
    else:
        raise NotImplementedException("Unrecognized player type {}".format(playerType))


def callMoveFunction(player, board):
    if game_rules.isInitialMove(board):
        return (
            player.selectInitialX(board)
            if player.symbol == "x"
            else player.selectInitialO(board)
        )
    else:
        return player.getMove(board)
