class Figure:
    def __init__(self, type, colour, position):
        self.type = type
        self.colour = colour
        self.position = position
        self.moved = False
        self.checked = False
        self.moves = {}
        self.legal = {}
