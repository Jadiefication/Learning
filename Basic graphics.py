# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
square_size = 100
square_x = 1280 // 2
square_y = 557
lowerst_background_point = 692


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #Makes the background
    background = pygame.image.load('background.jpg')
    background_rect = background.get_rect()
    background_rect.center = (1280 // 2, 720 // 2)
    screen.blit(background, background_rect)
    
    #Puts the stickman in the game
    image = pygame.image.load('stickman.png')
    image_rect = image.get_rect()
    image_rect.center = (square_x, square_y)
    screen.blit(image, image_rect)
    
    #Creates keybinds for the stickman
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        square_y -= 300 * dt
    if keys[pygame.K_s]:
        square_y += 300 * dt
    if keys[pygame.K_a]:
        square_x -= 300 * dt
    if keys[pygame.K_d]:
        square_x += 300 * dt
        
    #Checks if the stickman is out of frame    
    if square_y > 720:
        square_y = 1
    elif square_y < -99:
        square_y = 719    
    elif square_x > 1280:
        square_x = -99
    elif square_x < -99:
        square_x = 1280    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()