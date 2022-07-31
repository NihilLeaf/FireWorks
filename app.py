import pygame
import time
import random

pygame.init()
#Setting the window config
WIDTH, HEIGHT = 600, 400
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
#Class of projectiles
class projects:
    pass


#The firework class
class fireworks:
    pass


#creating the launchers class
class launcher:
    WIDTH = 20
    HEIGHT = 20
    COLOR = 'grey'

    def __init__(self, x, y, frequency):
        self.x = x
        self.y = y
        self.frequency = frequency #mileseconds
        self.start_time = time.time()
        self.fireworks = []
    
    #Fuction to Draw the launchers
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.WIDTH, self.HEIGHT))

    def launch(self):
        pass

    def loop(self, max_width, max_height):
        current_time = time.time()
        time_elapsed = current_time - self.start_time

        if time_elapsed * 1000 >= self.frequency:
            self.start_time = current_time
            self.launch()
#deffing color of background
def draw(launchers):
    win.fill('black')
    for launcher in launchers:
        launcher.draw(win)
    pygame.display.update()


#Starting the loop to the window
def main():
    run = True
    clock = pygame.time.Clock()
    launchers = [launcher(100, HEIGHT - launcher.HEIGHT, random.randint(2000, 4001))]

    #Run the program in 60 FPS
    while run:
        clock.tick(FPS)
    #Checking the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(launchers)
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()