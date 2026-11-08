class Player:
    def __init__(self, name="", symbole="", position=None):
        self.name = name
        self.symbole = symbole
        self.position = position

    def move(self, new_position):
        self.position = new_position

    def __str__(self):
        return f"Player {self.name} ({self.symbole}) is at position {self.position}"