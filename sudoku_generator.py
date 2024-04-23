import math
import random
class Sudoku_Generator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0] * row_length] * row_length
        self.box_length = int(math.sqrt(row_length))

    def get_board(self):
        return self.board

    def print_board(self):
        for i in range(0, len(self.board)):
            print(self.board[i])

    def valid_in_row(self, row, num):
        in_row = False
        for i in range(0, len(self.board[row])):
            if self.board[row][i] == num:
                in_row = True
                break
        return not in_row

    def valid_in_col(self, col, num):
        in_col = False
        for i in range(0, len(self.board)):
            if self.board[i][col] == num:
                in_col = True
                break
        return not in_col

    def valid_in_box(self, row_start, col_start, num):
        in_box = False
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if num == self.board[i][j]:
                    in_box = True
                    break
        return not in_box

    def is_valid(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        if self.valid_in_box(row_start, col_start, num) == True and self.valid_in_row(row,
                                                                                      num) == True and self.valid_in_col(
            col, num) == True:
            return True
        else:
            return False

    def fill_box(self, row_start, col_start):
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(l)
        self.board[row_start] = [0] * self.row_length
        self.board[row_start + 1] = [0] * self.row_length
        self.board[row_start + 2] = [0] * self.row_length
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.is_valid(i, j, l[((i - row_start) * 3) + (j - col_start)]):
                    self.board[i][j] = l[((i - row_start) * 3) + (j - col_start)]
                else:
                    continue

    def fill_diagonal(self):
        self.fill_box(6, 6)
        self.fill_box(3, 3)
        self.fill_box(0, 0)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        random_positions = []
        number_of_random_pos = 0
        while number_of_random_pos < self.removed_cells:
            random_position = (random.randint(0, 8), random.randint(0, 8))
            if random_position in random_positions:
                continue
            else:
                random_positions.append(random_position)
                number_of_random_pos += 1
        for i in range(0, len(random_positions)):
            x, y = random_positions[i][0], random_positions[i][1]
            self.board[x][y] = 0

    def generate_sudoku(self, removed):
        self.remove_cells()
        main_board = self.get_board()
        return main_board

    def generate_answer(self):
        self.fill_values()
        ans_board = self.get_board()
        return ans_board
