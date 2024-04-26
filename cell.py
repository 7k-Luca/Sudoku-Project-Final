import pygame
class Cell:
    def __init__(self, value, row, col, screen):
        # Constructor for the Cell class
        self.value = value
        self.sketch_value = 0
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        # Setter for this cell’s value
        self.value = value

    def set_sketched_value(self, value):
        # Setter for this cell’s sketched value
        self.sketch_value = value

    def draw(self):
        if self.sketch_value == 0:
            sketch_value = ''
        if self.value == 0:
            value = ''  # manages displaying no value if the cell has a zero value
        if self.sketch_value != 0:
            sketch_value = str(self.sketch_value)
        if self.value != 0:
            value = str(self.value)
        square_size = 70  # sets size of square
        cell_font = pygame.font.Font(None, 30)
        sketch_font = pygame.font.Font(None, 30)
        sketch_rect = pygame.Rect((self.row * square_size) + 5, (self.col * square_size) + 5, square_size + 5,
                           square_size + 5)
        value_temp = pygame.Rect((self.row * square_size), (self.col * square_size), square_size,
                            square_size)
        # uses pygame function to create a rectangle object with arguments (row,col,
        # square_size,square_size) to draw the cell
        sketch_surf = sketch_font.render(sketch_value, True, (122, 122, 122))
        value_surf = cell_font.render(value, True, (0, 0, 0))  # draws value with
        # arguments for value, True and color
        value_rect = value_surf.get_rect(center=value_temp.center)  # defines rectangle center
        self.screen.blit(sketch_surf, sketch_rect)
        self.screen.blit(value_surf, value_rect)  # uses .blit function to add image to screen
