import pygame,sys
from pygame.locals import *
from vector import Vector2


pygame.init()
screen=pygame.display.set_mode((800,600),0,32)

sprite=pygame.image.load('squidred.png').convert_alpha()

clock=pygame.time.Clock()

speed=.025
position=Vector2(100,100)
destination=Vector2()
heading=None


def display():
    global sprite,position
    screen.fill((0,0,0))
    screen.blit(sprite,(position.x,position.y))

def update():
    global position,destination,heading,speed,clock
    time_passed=0
    distance=0
    heading=Vector2.from_points((position.x,position.y),(destination.x,destination.y))
    heading.normalize()
    time_passed=clock.tick()
    distance=time_passed*speed
    position+=heading*distance
            

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type==MOUSEBUTTONDOWN:
            destination=Vector2(*event.pos)
             
        display()
        update()
        
        pygame.display.update()