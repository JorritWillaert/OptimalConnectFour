def choose_gamemode():
    """Return True if the player wants to play against the computer"""
    while True:
        gamemode = input("Do you want to play against an optimal computer? (y/n) ").lower().strip()
        if gamemode not in ['y', 'n', 'yes', 'no']:
            print("Invalid choice")
        else:
            if gamemode in ['y', 'yes']:
                return True
            return False
