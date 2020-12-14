from board import Board
from random import randint
import cpu

class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.size_horizontal = 7
        self.size_vertical = 6
        self.in_a_row = 4
        self.board = Board(self.size_horizontal, self.size_vertical)
        self.array_strings = ['1', '2', '3', '4', '5', '6', '7']

    def make_human_move(self, own, opponent):
        print(own.name + ", it is your turn. You are playing " + own.character)
        column = self.choose_move()
        row = self.board.check_row(column)
        if row == 0:
            self.board.remove_free_column(column)
        self.board.change_character(own.character, row, column)

    def make_cpu_move(self, own, opponent):
        value, column = cpu.cpu_min_max_algorithm(self, own, opponent)
        row = self.board.check_row(column)
        if row == 0:
            self.board.remove_free_column(column)
        self.board.change_character(own.character, row, column)
        return value

    def draw_board(self):
        self.board.draw_board()

    def victory(self, own, opponent, printing = True):
        """Check for victory"""
        row = self.size_vertical - 1
        column = 0
        while row >= 0:
            while column < self.size_horizontal:
                horizontal = diagonal_right = diagonal_left = vertical = False
                if column < self.size_horizontal - (self.in_a_row - 1):
                    horizontal = self.victory_row_right(row, column)
                if column < self.size_horizontal - (self.in_a_row - 1) and row > self.in_a_row - 2:
                    diagonal_right = self.victory_diagonal_right_up(row, column)
                if column > self.in_a_row - 2 and row > self.in_a_row - 2:
                    diagonal_left = self.victory_diagonal_left_up(row, column)
                if row > self.in_a_row - 2:
                    vertical = self.victory_column_up(row, column)
                if horizontal or diagonal_right or diagonal_left or vertical:
                    if printing:
                        self.print_victory(own)
                    return True
                column += 1
            column = 0
            row -= 1

    def print_victory(self, own):
        self.board.draw_board()
        print(own.name + ", congratulations! You've won!")

    def victory_row_right(self, row, column):
        running_char = self.board.get_character(row, column)
        if running_char == '.':
            return False
        for i in range(1, self.in_a_row):
            if self.board.get_character(row, column + i) != running_char:
                return False
        return True

    def victory_diagonal_right_up(self, row, column):
        running_char = self.board.get_character(row, column)
        if running_char == '.':
            return False
        for i in range(1, self.in_a_row):
            if self.board.get_character(row - i, column + i) != running_char:
                return False
        return True

    def victory_diagonal_left_up(self, row, column):
        running_char = self.board.get_character(row, column)
        if running_char == '.':
            return False
        for i in range(1, self.in_a_row):
            if self.board.get_character(row - i, column - i) != running_char:
                return False
        return True

    def victory_column_up(self, row, column):
        running_char = self.board.get_character(row, column)
        if running_char == '.':
            return False
        for i in range(1, self.in_a_row):
            if self.board.get_character(row - i, column) != running_char:
                return False
        return True

    def draw(self, printing = True):
        """Check for a draw (no more legal moves possible)"""
        if not self.board.get_free_columns():
            if printing:
                print("The game ended in a draw!")
            return True

    def choose_move(self):
        """Return a number between 0 and 6 (input - 1). Re-ask question if no legal move."""
        while True:
            move = input("Which column do you want to play? ").strip()
            if move not in self.array_strings:
                print("Invalid choice")
            else:
                column = int(move) - 1
                if column in self.board.get_free_columns():
                    return column
                print("Illegal move!")
                self.draw_board()

    def cpu_random_move(self):
        print("The CPU is doing a random move.")
        while True:
            column = randint(0, 6)
            if column in self.board.get_free_columns():
                break
        row = self.board.check_row(column)
        if row == 0:
            self.board.remove_free_column(column)
        self.board.change_character(own.character, row, column)


def choose_gamemode():
    """Return True if the player wants to play against the computer"""
    while True:
        cpu = input("Do you want to play against an optimal computer? (y/n) ").lower().strip()
        if cpu not in ['y', 'n', 'yes', 'no']:
            print("Invalid choice")
        else:
            if cpu in ['y', 'yes']:
                return True
            return False


def print_rules():
    print(
'''
Welcome to connect four!
The aim for both players is to make a straight line (vertical, horizontal or diagonal) of four pieces from your own color.
Moves are made alternatively, one by turn. Pieces slide downwards from upper holes, falling down to the last row or piling up on the last piece introduced in the same column.
The winner is the first player who gets a straight line made with four own pieces without gaps between them.

Have fun!
'''
    )
