class Player():
    def __init__(self, cpu, character):
        self.cpu = cpu
        self.name = self.ask_name()
        self.character = character
        self.laid_stones = 0

    def ask_name(self):
        if self.cpu:
            return "CPU"
        else:
            return input("What is your name? ")

    def increase_laid_stones(self):
        self.laid_stones += 1

    def decrease_laid_stones(self):
        self.laid_stones -= 1

    def get_laid_stones(self):
        return self.laid_stones
