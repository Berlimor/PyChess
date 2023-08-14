import pygame

WIDTH, HEIGHT = 1080, 720

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font('./fonts/Trajan Pro Regular.ttf', 20)
timer = pygame.time.Clock()
fps = 30

# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')

    # Handle different events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()