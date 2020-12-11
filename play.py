def main():
    print_rules()
    gamemode = choose_gamemode()
    player1 = new Player("Human")
    player2 = new Player(gamemode)
    play(player1, player2)

if __name__ == "__main__":
    main()
