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
