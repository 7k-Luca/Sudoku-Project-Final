import sys, pygame as pg
import pygame_tut_button

pg.init() # initializes pygame
size = 500, 500 # setting screen size to be this size (a square)
screen = pg.display.set_mode(size)
pg.display.set_caption("Soduko Game") # names the window at the top

# game variables
game_paused = False
menu_state = "main"

# fonts
font = pg.font.SysFont("arialblack", 20)
text_color = (255, 255, 255) # define colours

# load button images
resume_img = pg.image.load("images/button_resume.png").convert_alpha()
options_img = pg.image.load("images/button_options.png").convert_alpha()
quit_img = pg.image.load("images/button_quit.png").convert_alpha()
back_img = pg.image.load("images/button_back.png").convert_alpha()

# create button instances
resume_button = pygame_tut_button.Button(150, 125, resume_img, 1)
options_button = pygame_tut_button.Button(145, 250, options_img, 1)
quit_button = pygame_tut_button.Button(180, 375, quit_img, 1)
back_button = pygame_tut_button.Button(145, 250, back_img, 1)


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
        if menu_state == "main":
            if resume_button.draw(screen):
                game_paused = False
            if options_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                sys.exit()
        if menu_state == "options":
            if back_button.draw(screen):
                menu_state = "main"
    else:
        draw_text("Press SPACE to pause", font, text_color, 150, 250)


    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                game_paused = True
        if event.type == pg.QUIT:
            sys.exit()


running = True
while running:
    game_loop()
    pg.display.update()