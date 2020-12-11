from box import Box

class Board():
    def __init__(self):
        self.board = []
        for row in range(6):
            line = []
            for column in range(7):
                element = Box('.', (row, column))
                line.append(element)
            self.board.append(line)

    def draw_board(self):
        print()
        for row in range(6):
            print("    |", end = "")
            for column in range(7):
                print(self.board[row][column].get_character(), end="")
                print("|", end = "")
            print()
        print("   =================    ")
        print()
