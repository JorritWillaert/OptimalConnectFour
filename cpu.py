def calculate_utility(player):
    return 22 - player.get_laid_stones()

def cpu_min_max_algorithm(game, own, opponent):
    value, move = max_value(game, own, opponent, float("-inf"), float("inf"))
    return value, move

def max_value(game, own, opponent, alpha, beta):
    if game.victory(own, opponent, printing = False):
        utility = - calculate_utility(opponent)
        return (utility, None)
    if game.draw(printing = False):
        return (0, None)
    max_val = float("-inf")
    for column in range(game.size_horizontal):
        if column not in game.board.get_free_columns():
            continue
        row = game.board.check_row(column)
        if row == 0:
            game.board.remove_free_column(column)
        game.board.change_character(own.character, row, column)
        own.increase_laid_stones()
        value2, action2 = min_value(game, opponent, own, alpha, beta)
        #Restore (backtrack)
        own.decrease_laid_stones()
        game.board.change_character('.', row, column)
        if row == 0:
            game.board.add_free_column(column)
        if value2 > max_val:
            max_val = value2
            move = column
            alpha = max(alpha, max_val)
        if max_val >= beta:
            return max_val, move
    return max_val, move

def min_value(game, own, opponent, alpha, beta):
    if game.victory(own, opponent, printing = False):
        utility = calculate_utility(opponent)
        return (utility, None)
    if game.draw(printing = False):
        return (0, None)
    min_val = float("inf")
    for column in range(game.size_horizontal):
        if column not in game.board.get_free_columns():
            continue
        row = game.board.check_row(column)
        if row == 0:
            game.board.remove_free_column(column)
        game.board.change_character(own.character, row, column)
        own.increase_laid_stones()
        value2, action2 = max_value(game, opponent, own, alpha, beta)
        #Restore (backtrack)
        own.decrease_laid_stones()
        game.board.change_character('.', row, column)
        if row == 0:
            game.board.add_free_column(column)
        if value2 < min_val:
            min_val = value2
            move = column
            beta = min(beta, min_val)
        if min_val <= alpha:
            return min_val, move
    return min_val, move
