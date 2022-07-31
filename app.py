import pygame
import time
import random

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
#Class of projectiles
class projectiles:
    pass


#The firework class
class fireworks:
    RADIUS = 10
    MAX_PROJECTILES = 50
    MIN_PROJECTILES = 25
    PROJECTILE_V = 4

    def __init__(self, x, y, y_v, explode_height, color):
        self.x = x
        self.y = y
        self.y_v = y_v
        self.explode_height = explode_height
        self.color = color
        self.projectiles = []
        self.exploded = False
    
    def explode(self):
        self.exploded = True

    def move(self, max_width, max_height):
        if not self.exploded:
            self.y += self.y_v
            if self.y <= self.explode_height:
                self.explode()

    
    def draw(self, win):
        if not self.exploded:
            pygame.draw.circle(win, self.color, (self.x, self.y), self.RADIUS)

        for projectile in self.projectiles:
            projectile.draw(win)

#creating the launchers class
class Launcher:
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

        for firework in self.fireworks:
            firework.draw(win)

    def launch(self):
        color = random.choice(COLORS)
        explode_height = random.randrange(50, 400)
        firework = fireworks(self.x + self.WIDTH / 2, self.y, -5 , explode_height, color)
        self.fireworks.append(firework)

    def loop(self, max_width, max_height):
        current_time = time.time()
        time_elapsed = current_time - self.start_time

        if time_elapsed * 1000 >= self.frequency:
            self.start_time = current_time
            self.launch()

        fireworks_to_remove = []
        for firework in self.fireworks:
            firework.move(max_width, max_height)
            if firework.exploded and len(str(firework.projectiles == 0)):
                fireworks_to_remove.append(firework)
        
        for firework in fireworks_to_remove:
            self.fireworks.remove(firework)
 

#deffing color of background
def draw(launchers):
    win.fill('black')
    for Launcher in launchers:
        Launcher.draw(win)
    pygame.display.update()


#Starting the loop to the window
def main():
    run = True
    clock = pygame.time.Clock()
    launchers = [Launcher(100, HEIGHT - Launcher.HEIGHT, random.randint(2000, 4001))]

    #Run the program in 60 FPS
    while run:
        clock.tick(FPS)
    #Checking the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(launchers)

        for launcher in launchers:
            launcher.loop(WIDTH, HEIGHT)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()