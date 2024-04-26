import sys, pygame as pg
import pygame_tut_button

pg.init() # initializes pygame
size = 500, 500 # setting screen size to be this size (a square)
screen = pg.display.set_mode(size)
pg.display.set_caption("Sudoku Game") # names the window at the top

# game variables
game_paused = False
menu_state = "main"

# fonts
font = pg.font.SysFont("arialblack", 20)
text_color = (255, 255, 255) # define colours

# load button images
restart_img = pg.image.load("images/restart.png").convert_alpha()
reset_img = pg.image.load("images/reset.png").convert_alpha()
exit_img = pg.image.load("images/exit.png").convert_alpha()
back_img = pg.image.load("images/button_back.png").convert_alpha()
easy_img = pg.image.load("images/easy.png").convert_alpha()
medium_img = pg.image.load("images/medium.png").convert_alpha()
hard_img = pg.image.load("images/hard.png").convert_alpha()


# create button instances
restart_button = pygame_tut_button.Button(50, 450, restart_img, 1)
reset_button = pygame_tut_button.Button(190, 450, reset_img, 1)
exit_button = pygame_tut_button.Button(330, 450, exit_img, 1)
back_button = pygame_tut_button.Button(145, 250, back_img, 1)
easy_button = pygame_tut_button.Button(70,300, easy_img, 1)
medium_button = pygame_tut_button.Button(200,300, medium_img, 1)
hard_button = pygame_tut_button.Button(330,300, hard_img, 1)




def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def draw_background():
    screen.fill((52, 78, 91))

def game_loop():
    global game_paused
    global menu_state
    draw_background()
    # check if game is paused
    if game_paused == True:
        # if menu_state == "main":
        #     if resume_button.draw(screen):
        #         game_paused = False
        #     if options_button.draw(screen):
        #         menu_state = "options"
        #     if quit_button.draw(screen):
        #         sys.exit()
        # if menu_state == "options":
        #     if back_button.draw(screen):
        #         menu_state = "main"
        if menu_state == "game":
            draw_text("DRAW BOARD AND PLAY GAME HERE!!!!", font, text_color, 20,225)
            if back_button.draw(screen):
                game_paused = False
                menu_state = "main"
            if exit_button.draw(screen):
                sys.exit()
            if reset_button.draw(screen):
                pass
            if restart_button.draw(screen):
                pass

    else:
        draw_text("Welcome to Sudoku!", font, text_color, 140, 100)
        draw_text("Select game mode:", font, text_color, 140, 250)
        if easy_button.draw(screen):
            game_paused = True
            menu_state = "game"
        if medium_button.draw(screen):
            game_paused = True
            menu_state = "game"
        if hard_button.draw(screen):
            game_paused = True
            menu_state = "game"


    for event in pg.event.get():
    #     if event.type == pg.KEYDOWN:
    #         if event.key == pg.K_SPACE:
    #             game_paused = True
         if event.type == pg.QUIT:
             sys.exit()


running = True
while running:
    game_loop()
    pg.display.update()