from box import Box

class Board():
    def __init__(self, size_horizontal, size_vertical):
        self.board = []
        self.size_horizontal = size_horizontal
        self.size_vertical = size_vertical
        self.free_columns = list(range(self.size_horizontal))
        for row in range(self.size_vertical):
            line = []
            for column in range(self.size_horizontal):
                element = Box('.', (row, column))
                line.append(element)
            self.board.append(line)

    def draw_board(self):
        print()
        for row in range(self.size_vertical):
            print("    |", end = "")
            for column in range(self.size_horizontal):
                print(self.board[row][column].get_character(), end="")
                print("|", end = "")
            print()
        print("   ==" + self.size_horizontal * 2 * "=" + "=    ")
        print()

    def get_free_columns(self):
        return self.free_columns

    def remove_free_column(self, column):
        self.free_columns.remove(column)

    def add_free_column(self, column):
        self.free_columns.append(column)

    def check_row(self, column):
        row = self.size_vertical - 1
        while self.board[row][column].get_character() != ".":
            row -= 1
            assert(row >= 0)
        return row

    def change_character(self, character, row, column):
        self.board[row][column].set_character(character)

    def get_character(self, row, column):
        return self.board[row][column].get_character()
