import game_functions as gf
from game_functions import Game
from player import Player

from itertools import permutations

def play(player1, player2):
    players = (player1, player2)
    game = Game(player1, player2)
    while True:
        for own, opponent in permutations(players):
            own.increase_laid_stones()
            game.draw_board()
            if not own.cpu:
                game.make_human_move(own, opponent)
            else:
                game.make_cpu_move(own, opponent)
            if game.victory(own, opponent) or game.draw():
                return

def main():
    gf.print_rules()
    cpu = gf.choose_gamemode()
    player1 = Player(False, 'X')
    player2 = Player(cpu, 'O')
    play(player1, player2)

if __name__ == "__main__":
    main()
