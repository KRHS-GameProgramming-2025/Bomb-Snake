import pygame,math, sys, random


class Tail():
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        self.imagesUp = [pygame.image.load("Art/Snake/snake_Body_Down and Up.PNG")]
        self.imagesRight = [pygame.image.load("Art/Snake/snake_Body_Left and Right.PNG")]
        self.images = self.imagesUp

        self.frame = 0
        self.frameMax = len(self.images)-1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = startPos)
        
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.rad = (self.rect.height/2 + self.rect.width/2)/2
        
        self.maxSpeed = maxSpeed
        self.kind = "tail"
        
        self.animationTimer = 0
        self.animationTimerMax = 60/10
