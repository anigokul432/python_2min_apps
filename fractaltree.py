import random
from tracemalloc import start
import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fractal Tree")

FPS = 120

C_BG = pygame.Color(51,51,51)
C_OBJ = pygame.Color(115,204,250)

def DrawFractal(begin, size, theta, thickness, color):
    vec1 = pygame.Vector2(0,-size)
    vec1.rotate_ip(theta)   
    pygame.draw.line(WIN, color, begin, begin + vec1, thickness)

    if size > 1:
        if thickness - 1 < 2:
            thickness = 2
        DrawFractal(begin + vec1, size * .6, theta + pygame.time.get_ticks() * .01, thickness - 1, pygame.Color.lerp(color, (255,255,255), .15))
        DrawFractal(begin + vec1, size * .6, theta - pygame.time.get_ticks() * .01, thickness - 1, pygame.Color.lerp(color, (255,255,255), .15))



def Update():
    WIN.fill(C_BG) 

    startSize = 300
    DrawFractal(pygame.Vector2(WIDTH/2, HEIGHT), startSize, 0, 10, C_OBJ)
    
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:  
        clock.tick(FPS)      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        Update()      

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()