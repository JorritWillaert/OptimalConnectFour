class Player():
    def __init__(self, cpu, character):
        self.cpu = cpu
        self.name = self.ask_name()
        self.character = character

    def ask_name(self):
        if self.cpu:
            return "CPU"
        else:
            return input("What is your name? ")
