from ast import While
import pygame
pygame.init()
#Setting the window config
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FIREWORKS')

#Setting some constants
FPS = 60
COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (0, 255, 255),
    (255, 165, 0),
    (255, 255, 255),
    (230, 230, 255),
    (255, 192, 203),
]

#deffing color of background
def draw():
    win.fill('black')
    pygame.display.update()

#Starting the loop to the window
def main():
    run = True
    clock = pygame.time.Clock()
    #Run the program in 60 FPS
    while run:
        clock.tick(FPS)
    
    #Checking the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    draw()
    pygame.quit()
    quit()
if __name__ == '__main__':
    main()