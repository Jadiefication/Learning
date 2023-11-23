# Flappy bird
import pygame, random, math, Buttons

#TODO: add pillars and collision detection, allow the player to flop(cus its flappy bird), upgrades?, cleanup, polish the game, soundtracks, better textures, make the game playable in all resolutions

# pygame setup
pygame.init()
dt = 0
size = pygame.display.get_desktop_sizes()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
game_over_message_time = None
w, h = pygame.display.get_surface().get_size()

#bird variables
square_x = 1280 // 2
square_y = 1
max_speed = 3
starting_speed = 3
speed = starting_speed
show_stickman = True
show_game_over_message = False
square_y_ = 0

#gravity variables
grav = 0
jump = False

#background variables
scroll = 0

#Pause menu stuff
font = pygame.font.SysFont("arialblack", 50)
text_col = (255, 165, 0)
text_col2 = (0, 0, 0)
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

#draws the on the screen(not used for now)
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    
def waiting(cooldown):
    cooldown += 1
    if Start == True: 
        cooldown = 0
    return cooldown

#main game loop
Start = True
escape_key_pressed = False
left_click = False
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #gets what key is pressed
    keys = pygame.key.get_pressed()
    mb = pygame.mouse.get_pressed()
            
    #Creates keybinds for the stickman(for now mainly pause menu keybind)
    if keys[pygame.K_ESCAPE] and not escape_key_pressed and Start != True:
        escape_key_pressed = True
        if game_Paused:
            game_Paused = False
            menu_type = "main"
        else:
            game_Paused = True
            menu_type = "main"
    elif not keys[pygame.K_ESCAPE]:
        escape_key_pressed = False
    if keys[pygame.K_SPACE] and Start == True:
        Start = False
        show_game_over_message = False
    if mb[0] and not game_Paused and Start != True and not left_click:
        left_click = True
        if jump and cooldown == 0:
            jump = False
        else:
            jump = True        
    elif not mb[0]:
        left_click = False
     
    #getting the mouse position       
    px, py = pygame.mouse.get_pos()
    
    #uses the gravity
    grav += 0.5
    if game_Paused == False:
        speed += grav
    if speed > max_speed:
        speed = max_speed
    if game_Paused == False:
        if jump == False:
           square_y += speed
           cooldown = 0
        else:
            square_y -= 3
            cooldown = waiting(cooldown)
            if cooldown >= 30:
                jump = False

            
    #makes the pause background
    pbg = pygame.image.load("Pictures/Pause_Background.png")
    pbg_rect = pbg.get_rect()
    pbg_rect.center = (w // 2, h // 2)
    
    #makes the pause screen better
    ressumebg = pygame.image.load("Pictures/Play_Background.png").convert_alpha()
    resumebg_rect = ressumebg.get_rect()
    resumebg_rect.center = (25, 200)
    
    #prepares the background
    background = pygame.image.load("Pictures/background.jpg") 
    
    #prepare's the stickman    
    stlocation = "Pictures/stickman.png"
    stickman = pygame.image.load(stlocation)
    stickman_rect = stickman.get_rect()
    stickman_rect.center = (square_x, square_y)   
    
    #calculates how many background i need to fill the background
    background_width = background.get_width()
    tiles = math.ceil(1280 / background_width) + 1
    
    if Start != True:
        #prepare's the background
        bglocation = "Pictures/background.jpg"                          
        background = pygame.image.load(bglocation)
    
        #loads the scrolling background
        for i in range(0, tiles):        
            screen.blit(background, (i * background_width + scroll, 0) )
            screen.blit(stickman, stickman_rect)
    
        #makes the background scroll
        scroll -= 5 
        if abs(scroll) > background_width:
            scroll = 0
            
        #checks bird y position
        if square_y >= 720:
            Start = True
        if square_y <= 0:
            square_y = 1
            jump = False
    
    #pause menu
    if game_Paused == True:
        scroll = 0
        jump = False
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
                Start = True
            if resume_button.draw(screen):
                game_Paused = False
            if settings_button.draw(screen):
                menu_type = "options"
                pass
            
    if Start == True:
        square_y = 1
        for i in range(0, tiles): 
            screen.blit(background, (i * background_width + scroll, 0) )
        draw_text("Flappy Bird", font, text_col2, 521, 40 )     
        draw_text("Flappy Bird", font, text_col, 520, 40 )
        draw_text("Press SPACE to play the game", font, text_col2,  251, 620 )
        draw_text("Press SPACE to play the game", font, text_col,  250, 620 )
        game_Paused = False  
    
    #checks if the game is paused so it can stop the gravity        
    if game_Paused == False and show_stickman:
        stickman_rect.center = (square_x, square_y)

            
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()