"""Tic-tac-toe game."""


class TicTacToe:

    def __init__(self, n: int):
        self._n = n
        self._board = [[0] * n for i in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        """Move player with id <player> plays at the cell (row, col) of the board."""
        self._board[row][col] = player

        if self._horizontal_win(row, player) or self._vertical_win(col, player) \
            or (row == col and self._diagonal_win(player)) \
            or (col == self._n - 1 - row and self._anti_diagonal_win(player)):
            return player
        # no one wins
        return 0

    def _horizontal_win(self, row: int, player: int) -> bool:
        for col in range(self._n):
            if self._board[row][col] != player:
                return False
        return True

    def _vertical_win(self, col: int, player: int) -> bool:
        for row in range(self._n):
            if self._board[row][col] != player:
                return False
        return True

    def _diagonal_win(self, player: int) -> bool:
        for row in range(self._n):
            if self._board[row][row] != player:
                return False
        return True

    def _anti_diagonal_win(self, player: int) -> bool:
        for row in range(self._n):
            if self._board[row][self._n - 1 - row] != player:
                return False
        return True


class TicTacToeOpt:
    """Tic-tac-toe game."""
    def __init__(self, n: int):
        self._rows = n * [0]
        self._cols = n * [0]
        self._diagonal = 0
        self._anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        """Move player with id <player> plays at the cell (row, col) of the board."""
        n = len(self._rows)
        cur_player = 1 if player == 1 else -1

        # update currentPlayer in rows and cols arrays
        self._rows[row] += cur_player
        self._cols[col] += cur_player
        # update diagonal
        if row == col:
            self._diagonal += cur_player
        # update anti-diagonal
        if col == n - 1 - row:
            self._anti_diagonal += cur_player

        # check if the current player wins
        if abs(self._rows[row]) == n \
            or abs(self._cols[col]) == n \
            or abs(self._diagonal) == n \
            or abs(self._anti_diagonal) == n:
            return player

        # no one wins
        return 0
