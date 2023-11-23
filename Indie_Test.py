import pygame

pygame.init()
size = pygame.display.get_desktop_sizes()
screen = pygame.display.set_mode((size[1]))
running = True
clock = pygame.time.Clock()
cooldown = 0
cooldown2 = 0
f11 = False
Fullscreen = True
color = (255, 255, 255)
rs = (200, 100)
w, h = pygame.display.get_surface().get_size()
stickman_x = (w // 2)
stickman_y = (h // 2) 
show_stickman = True
space_pressed = False
dashed = False
grav = 0
max_speed = 3
starting_speed = 3
speed = starting_speed
jump = False

def waiting(cooldown2):
    cooldown2 += 1
    return cooldown2


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    background = pygame.Surface(screen.get_size())
    background.fill(color)
    screen.blit(background, (0, 0))
    
    if show_stickman:
        stlocation = "Pictures/New stickman.png"
        stickman = pygame.image.load(stlocation)
        stickman_rect = stickman.get_rect()
        stickman_rect.center = (stickman_x, stickman_y)
        screen.blit(stickman, stickman_rect)
    
    dash = pygame.image.load("Pictures/New Dash.png")
    dash_rect = dash.get_rect()
    dash_rect.center = (stickman_x - 100, stickman_y + 50)
    
    keys = pygame.key.get_pressed()
    mb = pygame.mouse.get_pressed() 
    if keys[pygame.K_F11] and not f11:
        f11 = True
        if Fullscreen:
            Fullscreen = False
            screen = pygame.display.set_mode((1280, 720))
        else:
            Fullscreen = True
            screen = pygame.display.set_mode((size[1]))
    elif not keys[pygame.K_F11]:
        f11 = False
    if keys[pygame.K_d]:
        stickman_x += 100 * dt
    if keys[pygame.K_a]:
        stickman_x -= 100 * dt
    if keys[pygame.K_s]:
       stickman_y += 100 * dt
    if keys[pygame.K_q]:
        dashed = True
        if keys[pygame.K_a]:
            stickman_x -= 500 * dt
            dash = pygame.image.load("Pictures/New Dash.png")
            dash_rect = dash.get_rect()
            dash_rect.center = (stickman_x + 100, stickman_y + 50) 
            dash = pygame.transform.flip(dash, True, False)
            screen.blit(dash, dash_rect)
            show_stickman = False
        elif keys[pygame.K_d]:
            stickman_x += 500 * dt
            dash = pygame.image.load("Pictures/New Dash.png")
            dash_rect = dash.get_rect()
            dash_rect.center = (stickman_x - 100, stickman_y + 50) 
            screen.blit(dash, dash_rect)
            show_stickman = False
        elif not keys[pygame.K_a] and not keys[pygame.K_d]:
            show_stickman = True
    elif not keys[pygame.K_q]:
        dashed = False
        show_stickman = True
    if keys[pygame.K_SPACE] and not space_pressed:
        space_pressed = True
        if jump and cooldown2 == 0:
            jump = False
        else:
            jump = True 
    elif not keys[pygame.K_SPACE]:
        space_pressed = False
        
    if any(keys) or any(mb):
        cooldown = 0
    
    if not any(keys) and not any(mb):    
        cooldown += 1
        
    grav += 0.5
    speed += grav
    if speed > max_speed:
        speed = max_speed
    if jump == False:
        stickman_y += speed
        cooldown2 = 0
    else:
        stickman_y -= 3
        cooldown2 = waiting(cooldown2)
        if cooldown2 >= 30:
            jump = False
            cooldown2 = 0
    
    if cooldown > 100:
        show_stickman = False
        afk = pygame.image.load("Pictures/New Ultimate.png")
        afk_rect = afk.get_rect()
        afk_rect.center = (stickman_x, stickman_y)
        screen.blit(afk, afk_rect)
        if cooldown > 200:
            show_stickman = True
            cooldown = 0
            
    if stickman_x > 1920:
        stickman_x = 1919
    elif stickman_x < 45:
        stickman_x = 46
        if dashed:
            stickman_x = 116
    elif stickman_x < 105 and dashed:
        stickman_x = 116
    if stickman_y > 968:
        stickman_y = 968
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()