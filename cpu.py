def calculate_utility(player):
    return 22 - player.get_laid_stones()

def cpu_min_max_algorithm(game, own, opponent):
    value, move = max_value(game, own, opponent)
    return move

def max_value(game, own, opponent):
    if game.victory(own, opponent, printing = False) or game.draw(printing = False):
        utility = calculate_utility(own)
        return (utility, None)
    max_val = float("-inf")
    for column in range(7):
        if column not in game.board.get_free_columns():
            continue
        row = game.board.check_row(column)
        if row == 0:
            game.board.remove_free_column(column)
        game.board.change_character(own.character, row, column)
        game.board.draw_board()
        own.increase_laid_stones()
        value2, action2 = min_value(game, own, opponent)
        #Restore (backtrack)
        own.decrease_laid_stones()
        game.board.change_character('.', row, column)
        if row == 0:
            game.board.add_free_column(column)
        if not action2:
            action2 = column
        if value2 > max_val:
            max_val = value2
            move = action2
    return max_val, move

def min_value(game, own, opponent):
    if game.victory(opponent, own, printing = False) or game.draw(printing = False):
        utility = calculate_utility(opponent)
        return (utility, None)
    min_val = float("inf")
    for column in range(7):
        if column not in game.board.get_free_columns():
            continue
        row = game.board.check_row(column)
        if row == 0:
            game.board.remove_free_column(column)
        game.board.change_character(opponent.character, row, column)
        game.board.draw_board()
        opponent.increase_laid_stones()
        value2, action2 = max_value(game, own, opponent)
        #Restore (backtrack)
        opponent.decrease_laid_stones()
        game.board.change_character('.', row, column)
        if row == 0:
            game.board.add_free_column(column)
        if not action2:
            action2 = column
        if value2 < min_val:
            min_val = value2
            move = action2
    return min_val, move
