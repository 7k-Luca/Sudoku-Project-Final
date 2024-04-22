from cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, row, col, screen) for col in range(9)] for row in range(9)]
        self.selected_cell = None

    def draw(self):
        cell_size = 50
        # Draw grid
        for i in range(10):
            if i % 3 == 0:
                thickness = 3
            else:
                thickness = 1
            pg.draw.line(self.screen, (0, 0, 0), (0, i * cell_size), (self.width, i * cell_size), thickness)
            pg.draw.line(self.screen, (0, 0, 0), (i * cell_size, 0), (i * cell_size, self.height), thickness)

        # Draw cells
        for row in self.cells:
            for cell in row:
                cell.draw()

    def select(self, row, col):
        if self.selected_cell:
            self.selected_cell.selected = False
        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True

    def click(self, x, y):
        cell_size = 50
        if 0 <= x < self.width and 0 <= y < self.height:
            col = x // cell_size
            row = y // cell_size
            return row, col
        else:
            return None

    def clear(self):
        if self.selected_cell:
            self.selected_cell.set_cell_value(0)
            self.selected_cell.set_sketched_value(0)

    def sketch(self, value):
        if self.selected_cell:
            self.selected_cell.set_sketched_value(value)

    def place_number(self, value):
        if self.selected_cell:
            self.selected_cell.set_cell_value(value)

    def reset_to_original(self):
        for row in self.cells:
            for cell in row:
                cell.set_cell_value(0)
                cell.set_sketched_value(0)

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def update_board(self):
        pass  # Not implemented yet

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:
                    return i, j
        return None

    def check_board(self):
        pass  # Not implemented yet