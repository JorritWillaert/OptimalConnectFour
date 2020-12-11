import game_functions as gf
from player import Player

def main():
    gf.print_rules()
    gamemode = gf.choose_gamemode()
    player1 = Player(False)
    player2 = Player(gamemode)
    #play(player1, player2)

if __name__ == "__main__":
    main()
