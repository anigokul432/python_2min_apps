from tracemalloc import start
import pygame
import math

pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Test")

FPS = 120

C_BG = (51,51,51)
C_OBJ = (115,204,250)
r = 5
k = .01
b = .97
restLength = 30

gravity = pygame.Vector2(0,0.01)
groundPlane = HEIGHT - 50

class Particle:
    def __init__(self, _pos):
        self.pos = _pos
        self.acc = pygame.Vector2(0,0)  
        self.vel = pygame.Vector2(0,0) 
        self.locked = False

    def calculate(self, _connectedParticle):
        pygame.draw.line(WIN, (255,255,255), self.pos, _connectedParticle.pos, 4)  
        if self.locked:
            return

        force = self.pos - _connectedParticle.pos
        x = force.magnitude() - restLength
        self.acc.update(-1 * force.normalize() * k * x + gravity)
        self.vel.update(.98 * self.vel + self.acc)

        targetPos = self.pos + self.vel
        self.pos.update(pygame.Vector2(self.constrain(targetPos[0], 0, WIDTH), self.constrain(targetPos[1], 0, groundPlane)))
            
    def constrain(self, val, min_val, max_val):
        return min(max_val, max(min_val, val))

    def applyForce(self, _force):
        self.acc.update(self.acc + _force)

    def show(self):
        pygame.draw.circle(WIN, C_OBJ, self.pos, r)

particles = []
count = 8
for i in range(0,count):
    particles.append(Particle(pygame.Vector2(50 + i * restLength, 100)))

def Update():
    WIN.fill(C_BG)    
    for i in range(0, len(particles)-1):
        particles[i].calculate(particles[i+1])
    
    for p in particles:
        p.show()

    pygame.draw.line(WIN, (160,160,160), (0, groundPlane) ,(WIDTH, groundPlane), 4)
        
    if pygame.mouse.get_pressed()[0]:
        particles[len(particles) - 1].vel.update(pygame.Vector2(0,0))
        particles[len(particles) - 1].pos.update(pygame.mouse.get_pos())

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