import pygame
pygame.init()

# Set up the display
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cursor Coordinates")
white = (255, 255, 255)
black = (0, 0, 0)
running = True
font = pygame.font.Font(None, 36)  # Choose a font and size

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get cursor position
    cursor_x, cursor_y = pygame.mouse.get_pos()

    # Clear the screen
    screen.fill(white)
    
    #Makes the background
    background = pygame.image.load('Pictures/background.jpg')
    background_rect = background.get_rect()
    background_rect.center = (1280 // 2, 720 // 2)
    screen.blit(background, background_rect)

    # Render text
    text = font.render(f"Cursor: ({cursor_x}, {cursor_y})", True, black)
    text_rect = text.get_rect()
    text_rect.center = (width // 2, height // 2)

    # Blit the text onto the screen
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
