# Example file showing a circle moving on screen
import pygame, random, math, Buttons

# pygame setup and variables used in the game
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
square_size = 100
square_x = random.randint(0,1280)
square_y = 453
scroll = 0

#Pause menu stuff
font = pygame.font.SysFont("arialblack", 40)
text_col = (0, 0, 0)
game_Paused = False
menu_type = "main"

#load buttons
resume_img = pygame.image.load("Pictures/Play.png").convert_alpha()
quit_img = pygame.image.load("Pictures/Quit.png").convert_alpha()
settings_img = pygame.image.load("Pictures/Setting.png").convert_alpha()

#create buttons
resume_button = Buttons.Button(75, 50, resume_img, 1)
quit_button = Buttons.Button(75, 250, quit_img, 1)
settings_button = Buttons.Button(75, 150, settings_img, 1)

#main game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))
        
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
    esc_key = 0  
    
    if abs(scroll) > background_width:
        scroll = 0
    
    #Creates keybinds for the stickman
    keys = pygame.key.get_pressed()
    if game_Paused == False:
        if keys[pygame.K_w]:
            square_y -= 300 * dt
        if keys[pygame.K_s]:
            square_y += 300 * dt
        if keys[pygame.K_a]:
            square_x -= 300 * dt
        if keys[pygame.K_d]:
            square_x += 300 * dt
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_Paused = True
   
    #Checks if the stickman is out of frame    
    if square_y > 720:
        square_y = 453
    elif square_y < 453:
        square_y = 453
        
    #pause menu
    if game_Paused == True:
        scroll = 0
        if menu_type == "main":
            if quit_button.draw(screen):
                running = False
            if resume_button.draw(screen):
                game_Paused = False
            if settings_button.draw(screen):
                menu_type = "options"
                pass

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()