from cell import Cell
import sys
import pygame
from sudoku_generator import Sudoku_Generator
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = 0
        self.selected_row = 0
        self.selected_col = 0
        self.mode = ''
        square_size = self.width // 9
        self.reset_rect = pygame.Rect(square_size * 3, self.height + 25, 75, 50)
        self.restart_rect = pygame.Rect(square_size * 4.5, self.height + 25, 80, 50)
        self.exit_rect = pygame.Rect(square_size * 6, self.height + 25, 75, 50)
        if difficulty == "Easy":
            self.difficulty = 30
        elif difficulty == "Medium":
            self.difficulty = 40
        elif difficulty == "Hard":
            self.difficulty = 50
        self.sudoku = Sudoku_Generator(9, self.difficulty)
        self.ans_board_temp = self.sudoku.generate_answer()
        self.ans_board = [[0 for i in range(9)] for i in range(9)]
        for i in range(0, len(self.ans_board_temp)):
            for j in range(0, len(self.ans_board_temp[i])):
                self.ans_board[i][j] = self.ans_board_temp[i][j]
        temp_board = self.sudoku.generate_sudoku(self.difficulty)
        self.board = [[0 for i in range(9)] for i in range(9)]
        for i in range(0, len(temp_board)):
            for j in range(0, len(temp_board[i])):
                if temp_board[i][j] == 0:
                    self.board[i][j] = Cell(0, i, j, self.screen)
                else:
                    self.board[i][j] = temp_board[i][j]

    def draw(self):
        cell_font = pygame.font.Font(None, 30)
        square_size = self.width // 9
        pygame.draw.line(self.screen, (0, 0, 0), (0, 0), (0, self.height), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 0), (self.width, 0), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.height), (self.width, self.height), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width, 0), (self.width, self.height), 3)
        pygame.draw.rect(self.screen, (0, 0, 0), self.reset_rect, 3)
        pygame.draw.rect(self.screen, (0, 0, 0), self.restart_rect, 3)
        pygame.draw.rect(self.screen, (0, 0, 0), self.exit_rect, 3)
        reset_surf = cell_font.render("Reset", True, (0, 0, 0))
        restart_surf = cell_font.render("Restart", True, (0, 0, 0))
        exit_surf = cell_font.render("Exit", True, (0, 0, 0))
        reset_rect = reset_surf.get_rect(center=self.reset_rect.center)
        restart_rect = restart_surf.get_rect(center=self.restart_rect.center)
        exit_rect = exit_surf.get_rect(center=self.exit_rect.center)
        self.screen.blit(reset_surf, reset_rect)
        self.screen.blit(restart_surf, restart_rect)
        self.screen.blit(exit_surf, exit_rect)
        for i in range(1, 9):
            line_width = 1
            if i % 3 == 0:
                line_width = 2
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * square_size), (self.width, i * square_size), line_width)
            pygame.draw.line(self.screen, (0, 0, 0), (i * square_size, 0), (i * square_size, self.height), line_width)
        for j in range(0, 9):
            for k in range(0, 9):
                if type(self.board[j][k]) != Cell:
                    cell_surf = cell_font.render(str(self.board[j][k]), True, (0, 0, 0))
                    rect = pygame.Rect((j) * square_size, (k) * square_size, square_size, square_size)
                    cell_rect = cell_surf.get_rect(center=rect.center)
                    self.screen.blit(cell_surf, cell_rect)
                elif type(self.board[j][k]) == Cell:
                    self.board[j][k].draw()

    def select(self, row, col):
        red = (255, 0, 0)
        square_size = (self.width // 9, self.height // 9)
        line_width = 3
        self.screen.fill((128, 170, 255))
        self.draw()
        self.selected_row = row - 1
        self.selected_col = col - 1
        rect = pygame.Rect((row - 1) * square_size[0], (col - 1) * square_size[1], square_size[0], square_size[1])
        pygame.draw.rect(self.screen, red, rect, line_width)

    def click(self, x, y, game_over):
        if game_over:
            square_size = self.width // 9
            row = x // square_size
            col = y // square_size
            self.selected_row = row
            self.selected_col = col
            if x < self.width - 3 and y < self.height - 3:
                self.select(row + 1, col + 1)
                return False
            elif self.reset_rect.collidepoint(x, y):
                self.reset_to_original()
                self.update_board()
                return False
            elif self.restart_rect.collidepoint(x, y):
                return True  # return to main menu
            elif self.exit_rect.collidepoint(x, y):
                sys.exit()

    def clear(self):
        self.board[self.selected_row][self.selected_col].set_cell_value(0)

    def sketch(self, value):
        self.board[self.selected_row][self.selected_col].set_sketched_value(value)

    def place_number(self, value):
        self.board[self.selected_row][self.selected_col].set_cell_value(value)

    def reset_to_original(self):
        self.selected_row = 0
        self.selected_col = 0
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                if type(self.board[i][j]) == Cell:
                    self.board[i][j].set_cell_value(0)
                    self.board[i][j].set_sketched_value(0)

    def is_full(self):
        for i in range(9):
            for j in range(9):
                if type(self.board[i][j]) == Cell and self.board[i][j].value == 0:
                    return False
        return True

    def update_board(self):
        self.screen.fill((128, 170, 255))
        self.draw()
        pygame.display.update()

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if type(self.board[i][j]) == Cell and self.board[i][j].value == 0:
                    return i, j
        return None

    def check_board(self):
        win = False
        for i in range(9):
            for j in range(9):
                if type(self.board[i][j]) == Cell:
                    if int(self.board[i][j].value) == self.ans_board[i][j]:
                        win = True
                    elif int(self.board[i][j].value) != self.ans_board[i][j]:
                        return False
        return win
