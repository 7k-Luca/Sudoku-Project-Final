import sys, pygame as pg
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.font = pygame.font.SysFont('Arial', 40)

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        cell_size = 50
        x = self.col * cell_size
        y = self.row * cell_size

        # Draw cell outline
        pg.draw.rect(self.screen, (0, 0, 0), (x, y, cell_size, cell_size), 1)

        # Draw value if not zero
        if self.value != 0:
            text = self.font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            self.screen.blit(text, text_rect)

        # Draw sketched value if not zero
        if self.sketched_value != 0:
            sketched_text = self.font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(sketched_text, (x + 5, y + 5))

        # Draw selection highlight
        if self.selected:
            pg.draw.rect(self.screen, (255, 0, 0), (x, y, cell_size, cell_size), 3)
