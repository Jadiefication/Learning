# Example file showing a circle moving on screen
import pygame, random, math, Buttons

# pygame setup and variables used in the game
pygame.init()
grav = 0
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
square_size = 100
square_x = 1280 // 2
square_y = 1
scroll = 0
max_speed = 3
starting_speed = 3
is_mouse_button_pressed = False

speed = starting_speed

#Pause menu stuff
font = pygame.font.SysFont("arialblack", 40)
text_col = (0, 0, 0)
game_Paused = False
menu_type = "main"

#load buttons
resume_img = pygame.image.load("Pictures/Play.png").convert_alpha()
quit_img = pygame.image.load("Pictures/Quit.png").convert_alpha()
settings_img = pygame.image.load("Pictures/Settings.png").convert_alpha()

#create buttons
resume_button = Buttons.Button(25, 210, resume_img, 1)
quit_button = Buttons.Button(25, 410, quit_img, 1)
settings_button = Buttons.Button(25, 310, settings_img, 1)

#main game loop
escape_key_pressed = False
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    px, py = pygame.mouse.get_pos()
    
    grav += 0.5
    if game_Paused == False:
        speed += grav
    
    if speed > max_speed:
        speed = max_speed
     
    if game_Paused == False:   
        square_y += speed
        
    if square_y > 720:
        square_y = 1
        speed = starting_speed
        is_jumping = False
    
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))
        
    #makes the pause background
    pbg = pygame.image.load("Pictures/Pause_Background.png")
    pbg_rect = pbg.get_rect()
    pbg_rect.center = (1280 // 2, 720 // 2)
    
    #makes the pause screen better
    ressumebg = pygame.image.load("Pictures/Play_Background.png").convert_alpha()
    resumebg_rect = ressumebg.get_rect()
    resumebg_rect.center = (25, 200)
    
    #prepare's the stickman    
    stlocation = "Pictures/stickman.png"
    stickman = pygame.image.load(stlocation)
    stickman_rect = stickman.get_rect()
    stickman_rect.center = (square_x, square_y)
            
    #prepare's the background
    bglocation = "Pictures/background.jpg"                          
    background = pygame.image.load(bglocation)
    
    #calculates how many background i need to fill the background + fills the background
    background_width = background.get_width()
    tiles = math.ceil(1280 / background_width) + 1
    for i in range(0, tiles):        
        screen.blit(background, (i * background_width + scroll, 0) )
        screen.blit(stickman, stickman_rect)
    
    scroll -= 5 
    
    if abs(scroll) > background_width:
        scroll = 0
        
    
    #Creates keybinds for the stickman
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE] and not escape_key_pressed:
        escape_key_pressed = True
        if game_Paused:
            game_Paused = False
        else:
            game_Paused = True
    elif not keys[pygame.K_ESCAPE]:
        escape_key_pressed = False
        
    #pause menu
    if game_Paused == True:
        scroll = 0
        screen.blit(pbg, pbg_rect)
        if menu_type == "main":
            if settings_button.rect.collidepoint(px, py):
                resumebg_rect.center = settings_button.rect.center
                screen.blit(ressumebg, resumebg_rect)
            if quit_button.rect.collidepoint(px, py):
                resumebg_rect.center = quit_button.rect.center
                screen.blit(ressumebg, resumebg_rect)
            if resume_button.rect.collidepoint(px, py):
                resumebg_rect.center = resume_button.rect.center
                screen.blit(ressumebg, resumebg_rect)
            if quit_button.draw(screen):
                running = False
            if resume_button.draw(screen):
                game_Paused = False
            if settings_button.draw(screen):
                menu_type = "options"
                pass
            
    if game_Paused == False:
        stickman_rect.center = (square_x, square_y)
            
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()