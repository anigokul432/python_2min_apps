from tracemalloc import start
import pygame
from datetime import datetime
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Clock")

FPS = 120

C_BG = (51,51,51)
C_OBJ = (200,200,200)
C_HOUR = (102,178,255)
C_MINUTE = (255,102,102)
C_SECOND = (160,160,160)

def Update():
    WIN.fill(C_BG) 

    clockSize = 370

    second = datetime.now().time().second + datetime.now().time().microsecond/1000000
    minute = datetime.now().time().minute + second / 60
    hour = datetime.now().time().hour + minute / 60

    pygame.draw.circle(WIN, C_OBJ, (WIDTH/2,HEIGHT/2), clockSize, 4)

    DrawLine(clockSize * .7, second * 6, C_SECOND)
    DrawLine(clockSize * .9, minute * 6, C_MINUTE)
    DrawLine(clockSize * .5, hour % 12 / 12 * 360, C_HOUR)

    for i in range(60):
        if i % 5 == 0:
            w = 20
        else:
            w = 10
        startDist = clockSize
        endDist = clockSize - w
        start = pygame.Vector2(WIDTH/2 + startDist * math.cos(math.radians(i * 6)), HEIGHT/2 + startDist * math.sin(math.radians(i*6)))
        end = pygame.Vector2(WIDTH/2 + endDist * math.cos(math.radians(i * 6)), HEIGHT/2 + endDist * math.sin(math.radians(i*6)))
        pygame.draw.aaline(WIN, C_OBJ, start, end, 1)

    pygame.display.update()

def DrawLine(r, a, c):
    x = r * math.cos(math.radians(a - 90))
    y = r * math.sin(math.radians(a - 90))
    pygame.draw.line(WIN,c,(WIDTH/2,HEIGHT/2), (WIDTH/2 + x,HEIGHT/2 + y), 5)

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