import pygame
import random
import sys
from board import Board
from cell import Cell


if __name__ == '__main__':
    pygame.init()
    height = 730
    width = 630
    rect_height = 50
    rect_width = 125
    rect_x = 100
    rect_y = 425
    original_pos = pygame.Rect((height + 100, width + 100, 1, 1))
    ending_rect = original_pos
    rect_easy = original_pos
    rect_medium = original_pos
    rect_hard = original_pos
    restarting_rect = original_pos
    finished = False
    in_main_menu = True
    game_over_loose = False
    game_over_win = False
    screen = pygame.display.set_mode((width, height), flags=pygame.SCALED)
    pygame.display.set_caption('Sudoku')
    text_f = pygame.font.Font(None, 70)
    option_font = pygame.font.Font(None, 35)
    icon = pygame.image.load(
        'image.png').convert()
    screen.blit(icon, (0, 0))
    board = None
    random.seed(random.randint(0, 100000000))


    def draw_rect(pos, color='Grey', width=0):
        pygame.draw.rect(screen, color, pos, width)

        return pygame.Rect(pos)


    def write_text(text, pos, color='Grey', text_font=text_f):
        text_surf = text_font.render(text, 0, color)
        text_rect = text_surf.get_rect(center=pos)
        screen.blit(text_surf, text_rect)


    def draw_starting_screen():
        icon = pygame.image.load('image.png').convert()
        screen.blit(icon, (0, 0))
        draw_rect((50, (height // 2 - 225), 540, 50), 'black')
        draw_rect((50, (height // 2 - 125), 540, 50), 'black')
        write_text('Welcome To Sudoku', (width // 2, height // 2 - 200))
        write_text('Select Game Mode', (width // 2, height // 2 - 100))
        rect_easy = draw_rect((rect_x, rect_y + 50, rect_width, rect_height))
        rect_medium = draw_rect((rect_x + 150, rect_y + 50, rect_width, rect_height))
        rect_hard = draw_rect((rect_x + 300, rect_y + 50, rect_width, rect_height))
        write_text('Easy', (rect_x + 60, rect_y + 75), 'Black', text_font=option_font)
        write_text('Medium', (rect_x + 210, rect_y + 75), 'Black', text_font=option_font)
        write_text('Hard', (rect_x + 360, rect_y + 75), 'Black', text_font=option_font)
        return rect_easy, rect_medium, rect_hard


    def draw_ending_screen_win():
        icon = pygame.image.load('image.png').convert()
        screen.blit(icon, (0, 0))
        draw_rect(((width // 2 - 57.5), (height // 2 - 225), rect_width, 50), 'Grey')
        write_text('You Won!', (width // 2, height // 2 - 200), 'black', text_font=option_font)
        rect = draw_rect((width // 2 - 50, height // 2, rect_width, rect_height))
        write_text('Exit', (width // 2 + 10, height // 2 + 25), 'black', text_font=option_font)
        return rect


    def draw_ending_screen_loose():
        icon = pygame.image.load('image.png').convert()
        screen.blit(icon, (0, 0))
        draw_rect(((width // 2 - 57.5), (height // 2 - 225), rect_width, 50), 'Grey')
        write_text('You lost!', (width // 2, height // 2 - 200), 'black', text_font=option_font)
        rect = draw_rect((width // 2 - 50, height // 2, rect_width, rect_height))
        write_text('Restart', (width // 2 + 10, height // 2 + 25), 'black', text_font=option_font)
        return rect


    def return_to_original(*args):
        for i in args:
            kwargs = original_pos


    rect_easy, rect_medium, rect_hard = draw_starting_screen()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game_over_win:
                ending_rect = draw_ending_screen_win()
                if ending_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(screen, (0, 0, 0), ending_rect, 3)
                else:
                    ending_rect = draw_ending_screen_win()
            if game_over_loose:
                board.reset_to_original()

                if restarting_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(screen, (0, 0, 0), restarting_rect, 3)
                else:
                    restarting_rect = draw_ending_screen_loose()
            if event.type == pygame.TEXTINPUT:
                if not in_main_menu and not game_over_win and not game_over_loose:
                    if type(board.board[board.selected_row][board.selected_col]) == Cell:
                        try:
                            value = int(event.text)
                        except:
                            value = 0
                        board.draw()
                        temp_rect = pygame.Rect((board.selected_row * 70) + 5, (board.selected_col * 70) + 5, 62, 62)
                        board.select(board.selected_row + 1, board.selected_col + 1)
                        pygame.draw.rect(screen, (128, 170, 255), temp_rect, 0)
                        value_font = pygame.font.Font(None, 30)
                        value_temp = pygame.Rect((board.selected_row * 70), (board.selected_col * 70), 70, 70)
                        temp_value = ' '
                        if board.board[board.selected_row][board.selected_col].value != 0:
                            temp_value = str(board.board[board.selected_row][board.selected_col].value)
                        value_surf = value_font.render(temp_value, True, (0, 0, 0))
                        value_rect = value_surf.get_rect(center=value_temp.center)
                        screen.blit(value_surf, value_rect)
                        sketch_font = pygame.font.Font(None, 30)
                        sketch_rect = pygame.Rect((board.selected_row * 70) + 5, (board.selected_col * 70) + 5, 75, 75)
                        sketch_surf = sketch_font.render(str(value), True, (122, 122, 122))
                        screen.blit(sketch_surf, sketch_rect)
                        board.board[board.selected_row][board.selected_col].set_sketched_value(str(value))
            if event.type == pygame.KEYDOWN:
                if not in_main_menu:
                    if not game_over_loose and not game_over_win:
                        if event.key == pygame.K_UP:
                            if board.selected_col > 0:
                                board.selected_col -= 1
                                board.select(board.selected_row + 1, board.selected_col + 1)
                                pygame.display.update()
                        if event.key == pygame.K_DOWN:
                            if board.selected_col < 8:
                                board.selected_col += 1
                                board.select(board.selected_row + 1, board.selected_col + 1)
                                pygame.display.update()
                        if event.key == pygame.K_LEFT:
                            if board.selected_row > 0:
                                board.selected_row -= 1
                                board.select(board.selected_row + 1, board.selected_col + 1)
                                pygame.display.update()
                        if event.key == pygame.K_RIGHT:
                            if board.selected_row < 8:
                                board.selected_row += 1
                                board.select(board.selected_row + 1, board.selected_col + 1)
                                pygame.display.update()
                    if event.key == pygame.K_RETURN:
                        if type(board.board[board.selected_row][board.selected_col]) == Cell:
                            if board.board[board.selected_row][board.selected_col].sketch_value != 0:
                                board.place_number(board.board[board.selected_row][board.selected_col].sketch_value)
                                board.sketch(0)
                                board.select(board.selected_row + 1, board.selected_col + 1)
                    if event.key == pygame.K_BACKSPACE:
                        if type(board.board[board.selected_row][board.selected_col]) == Cell:
                            value = 0
                            board.sketch(value)
                            board.update_board()
                            board.select(board.selected_row + 1, board.selected_col + 1)
                    if board.is_full():
                        if not board.check_board():
                            game_over_loose = True
                            continue
                        if board.check_board():
                            game_over_win = True
                            continue

            if in_main_menu:
                if rect_easy.collidepoint(pygame.mouse.get_pos()):
                    draw_starting_screen()
                    pygame.draw.rect(screen, (0, 0, 0), rect_easy, 3)
                elif rect_medium.collidepoint(pygame.mouse.get_pos()):
                    draw_starting_screen()
                    pygame.draw.rect(screen, (0, 0, 0), rect_medium, 3)
                elif rect_hard.collidepoint(pygame.mouse.get_pos()):
                    draw_starting_screen()
                    pygame.draw.rect(screen, (0, 0, 0), rect_hard, 3)
                else:
                    draw_starting_screen()

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if ending_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                if restarting_rect.collidepoint(pygame.mouse.get_pos()):
                    game_over_loose = False
                    return_to_original(restarting_rect)
                    restarting_rect = draw_ending_screen_loose()
                if in_main_menu:
                    if rect_easy.collidepoint(pygame.mouse.get_pos()):
                        board = Board(630, 630, screen, 'Easy')
                        board.update_board()
                        in_main_menu = False
                        continue
                    if rect_medium.collidepoint(pygame.mouse.get_pos()):
                        board = Board(630, 630, screen, 'Medium')
                        board.update_board()
                        in_main_menu = False
                        continue
                    if rect_hard.collidepoint(pygame.mouse.get_pos()):
                        board = Board(630, 630, screen, 'Hard')
                        board.update_board()
                        in_main_menu = False
                        continue

                if not in_main_menu:
                    if not game_over_win and not game_over_loose:
                        mousepos = pygame.mouse.get_pos()
                        if board.click(mousepos[0], mousepos[1], not game_over_win or not game_over_loose):
                            in_main_menu = True
                            rect_easy, rect_medium, rect_hard = draw_starting_screen()
                            continue
                    if board.is_full():
                        if not board.check_board():
                            game_over_loose = True
                            continue
                        if board.check_board():
                            game_over_win = True
                            continue
            if not in_main_menu:
                if not game_over_loose and not game_over_win:
                    if board.reset_rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.draw.rect(screen, (0, 0, 0), board.restart_rect, 3)
                        pygame.draw.rect(screen, (255, 0, 0), board.reset_rect, 3)
                        pygame.draw.rect(screen, (0, 0, 0), board.exit_rect, 3)
                    elif board.restart_rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.draw.rect(screen, (255, 0, 0), board.restart_rect, 3)
                        pygame.draw.rect(screen, (0, 0, 0), board.reset_rect, 3)
                        pygame.draw.rect(screen, (0, 0, 0), board.exit_rect, 3)
                    elif board.exit_rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.draw.rect(screen, (0, 0, 0), board.restart_rect, 3)
                        pygame.draw.rect(screen, (0, 0, 0), board.reset_rect, 3)
                        pygame.draw.rect(screen, (255, 0, 0), board.exit_rect, 3)
                    else:
                        pygame.draw.rect(screen, (0, 0, 0), board.restart_rect, 3)
                        pygame.draw.rect(screen, (0, 0, 0), board.reset_rect, 3)
                        pygame.draw.rect(screen, (0, 0, 0), board.exit_rect, 3)
        pygame.display.update()

