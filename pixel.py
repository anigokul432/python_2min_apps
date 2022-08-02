import random
from tracemalloc import start
import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fractal Tree")

FPS = 120

C_BG = (51,51,51)
C_OBJ = (115,204,250)

def Update():

    points = []
    numPoints = 10

    for i in range(0,numPoints):
        points.append(pygame.Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT)))

    for p in points:
        pygame.draw.circle(WIN, C_OBJ, p, 5)

    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            distances = []
            for i in range(0, len(points)):
                distances.append(pygame.Vector2.distance_to(pygame.Vector2(x,y), points[i]))
            maxDist = pygame.Vector2.distance_to(pygame.Vector2(0,0), pygame.Vector2(WIDTH,HEIGHT))/2
            distances.sort()
            n = 0
            noise = distances[n]
            WIN.set_at((x,y), (255*(1-noise/maxDist),255*(1-noise/maxDist),255*(1-noise/maxDist))) 
    

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    Update() 
    run = True
    while run:  
        clock.tick(FPS)      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False     

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()