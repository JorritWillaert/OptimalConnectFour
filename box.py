class Box():
    def __init__(self, character, position):
        self.character = character
        self.position = position

    def get_character(self):
        return self.character

    def set_character(self, character):
        self.character = character
