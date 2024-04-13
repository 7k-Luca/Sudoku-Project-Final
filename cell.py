class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    """
        Setter for this cell's value
    """
    def set_cell_value(self, value):
        pass

    """
        Setter for this cell's sketched value
    """
    def set_sketched_value(self, value):
        pass

    def draw(self):
        pass