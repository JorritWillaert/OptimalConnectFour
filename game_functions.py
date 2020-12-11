from board import Board

class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()

    def make_human_move(self, own, opponent):
        None

    def make_cpu_move(self, own, opponent):
        None

    def draw_board(self):
        #self.board.draw_board()
        None

    def victory(self, own, opponent):
        """Check for victory"""
        None

    def draw(self):
        """Check for a draw (no more legal moves possible)"""
        None

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
