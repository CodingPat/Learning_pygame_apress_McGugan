import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen=pygame.display.set_mode((800,600),0,32)

img_red_squid=pygame.image.load("squidred.png").convert()
clock=pygame.time.Clock()
frame_nr=0

class Squid():
    def __init__(self,pos,img,speed):
        self.x,self.y=pos
        self.img=pygame.image.load(img).convert()
        self.speed=speed
    def update(self):
        self.x+=self.speed
        if self.x>screen.get_width():
            self.x=0
    def display(self):
        screen.blit(self.img,(self.x,self.y))

class SlowSquid(Squid):
    def __init__(self,pos,img,speed):
        Squid.__init__(self,pos,img,speed)
    def update(self,frame_nr):
        if frame_nr%5==0:
            self.x+=self.speed
        if self.x>screen.get_width():
            self.x=0

squid1=Squid((0,50),"squidred.png",5)
squid2=SlowSquid((0,150),"squidred.png",5)



while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        
    squid1.update()
    squid2.update(frame_nr)
    screen.fill((0,0,0))
    squid1.display()
    squid2.display()
    
    clock.tick(30)
    
    pygame.display.update()
    frame_nr+=1
    
