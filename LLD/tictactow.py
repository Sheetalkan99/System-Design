# Import Enum for Symbol and GameStatus
from enum import Enum
from typing import List


# ----------------------------------------
# Enums for Symbol and Game Status
# ----------------------------------------

class Symbol(Enum):
    """Represents allowed symbols for the game board: X or O"""
    X = "X"
    O = "O"


class GameStatus(Enum):
    """Tracks the current state of the game"""
    IN_PROGRESS = 1
    WIN = 2
    DRAW = 3


# ----------------------------------------
# Cell Class
# ----------------------------------------

class Cell:
    """
    Represents a single cell on the board.
    Each cell may or may not have a symbol.
    """

    def __init__(self):
        self.symbol = None  # Initially empty

    def is_empty(self):
        """Returns True if the cell is unoccupied"""
        return self.symbol is None

    def set_symbol(self, symbol):
        """
        Sets the symbol in the cell if it's empty.
        Returns True if successful, False if already occupied.
        """
        if self.is_empty():
            self.symbol = symbol
            return True
        return False


# ----------------------------------------
# Player Class
# ----------------------------------------

class Player:
    """
    Represents a player in the game.
    Each player has a name and a symbol (X or O).
    """

    def __init__(self, name: str, symbol: Symbol):
        self.name = name
        self.symbol = symbol


# ----------------------------------------
# Board Class
# ----------------------------------------

class Board:
    """
    Represents the NxN game board and its logic.
    Handles move placement, checking for wins and draws.
    """

    def __init__(self, size: int):
        self.size = size
        self.grid = [[Cell() for _ in range(size)] for _ in range(size)]  # NxN grid of Cells

    def display(self):
        """Prints the current board status"""
        for row in self.grid:
            row_values = [cell.symbol.value if cell.symbol else "_" for cell in row]
            print(" | ".join(row_values))
        print()

    def make_move(self, row, col, symbol: Symbol):
        """
        Attempts to place a symbol in a cell.
        Returns True if successful, False if invalid.
        """
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.grid[row][col].set_symbol(symbol)
        return False

    def is_full(self):
        """Checks if all cells on the board are filled (used for detecting draw)"""
        return all(not cell.is_empty() for row in self.grid for cell in row)

    def check_winner(self, symbol: Symbol):
        """Checks if the given symbol has won the game (row, column, diagonal)"""
        size = self.size

        # Check rows
        for row in self.grid:
            if all(cell.symbol == symbol for cell in row):
                return True

        # Check columns
        for col in range(size):
            if all(self.grid[row][col].symbol == symbol for row in range(size)):
                return True

        # Check left-to-right diagonal
        if all(self.grid[i][i].symbol == symbol for i in range(size)):
            return True

        # Check right-to-left diagonal
        if all(self.grid[i][size - 1 - i].symbol == symbol for i in range(size)):
            return True

        return False


# ----------------------------------------
# Game Class
# ----------------------------------------

class Game:
    """
    Manages the entire game flow.
    Handles player turns, move validation, game status, and interaction with the board.
    """

    def __init__(self, player1: Player, player2: Player, board_size: int):
        self.board = Board(board_size)
        self.players = [player1, player2]
        self.current_index = 0  # 0 or 1: tracks whose turn it is
        self.status = GameStatus.IN_PROGRESS

    def switch_turn(self):
        """Switch the current player index (0 <-> 1)"""
        self.current_index = 1 - self.current_index

    def start(self):
        """Starts and runs the game loop"""
        print("🎮 Game Started!\n")
        self.board.display()

        # Keep playing while game is not over
        while self.status == GameStatus.IN_PROGRESS:
            player = self.players[self.current_index]
            print(f"{player.name}'s turn ({player.symbol.value}):")

            # Get input from player
            try:
                row = int(input("Enter row (0-based index): "))
                col = int(input("Enter col (0-based index): "))
            except ValueError:
                print("❌ Invalid input. Please enter integers.")
                continue

            # Validate and make the move
            if not self.board.make_move(row, col, player.symbol):
                print("❌ Invalid move. Cell is already occupied or out of bounds.")
                continue

            self.board.display()

            # Check if player has won
            if self.board.check_winner(player.symbol):
                print(f"🏆 {player.name} wins!")
                self.status = GameStatus.WIN
                break

            # Check for draw
            if self.board.is_full():
                print("⚖️ It's a draw!")
                self.status = GameStatus.DRAW
                break

            # Switch to next player
            self.switch_turn()


# ----------------------------------------
# Game Entry Point
# ----------------------------------------

if __name__ == "__main__":
    # Get player names
    name1 = input("Enter Player 1 name: ")
    name2 = input("Enter Player 2 name: ")

    # Create Player objects with symbols
    player1 = Player(name1, Symbol.X)
    player2 = Player(name2, Symbol.O)

    # Define board size (3x3 for classic game)
    board_size = 3

    # Create and start the game
    game = Game(player1, player2, board_size)
    game.start()
