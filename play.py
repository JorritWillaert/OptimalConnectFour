import game_functions as gf
from game_functions import Game
from player import Player

from itertools import permutations

def play(player1, player2, array):
    players = (player1, player2)
    game = Game(player1, player2)
    while True:
        for own, opponent in permutations(players):
            if array:
                column = array.pop(0) - 1
                row = game.board.check_row(column)
                if row == 0:
                    game.board.remove_free_column(column)
                game.board.change_character(own.character, row, column)
                own.increase_laid_stones()

            else:
                value = game.make_cpu_move(own, opponent)
                own.increase_laid_stones()
                game.draw_board()
                print("Utility:", value)
                #if not own.cpu:
                #    game.make_human_move(own, opponent)
                #else:
                #    game.make_cpu_move(own, opponent)
                return value
            if game.victory(own, opponent) or game.draw():
                return

def main():
    gf.print_rules()
    cpu = gf.choose_gamemode()
    misses = 0
    count = 0
    with open("testset.txt") as f:
        lines = f.readlines()
        for line in lines:
            player1 = Player(cpu, 'X')
            player2 = Player(cpu, 'O')
            master_array = line.split()
            array = [int(char) for char in master_array[0]]
            value = play(player1, player2, array)
            count += 1
            if int(master_array[1]) == value:
                print("OK. Number of misses:", misses, ". Already cheched:", count)
            else:
                misses += 1
                print("Miss. Number of misses:", misses, ". Already cheched:", count)

if __name__ == "__main__":
    main()
