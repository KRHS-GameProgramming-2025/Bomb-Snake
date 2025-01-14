import pygame, sys, math
class Head():
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        #fix images
        self.imagesUp = [pygame.image.load("images/Playerball/playerBall-UP.PNG")]
        self.imagesDown = [pygame.image.load("images/Playerball/playerBall-DOWN.PNG")]
        self.imagesLeft = [pygame.image.load("images/Playerball/playerBall-LEFT.PNG")]
        self.imagesRight = [pygame.image.load("images/Playerball/playerBall-RIGHT.PNG")]
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
        self.kind = "head"

    def goKey(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
            self.images =self.imagesLeft
        elif direction == "right":
            self.speedx = self.maxSpeed
            self.images =self.imagesRight
        elif direction == "up":
            self.speedy = -self.maxSpeed
            self.images =self.imagesUp
        elif direction == "down":
            self.speedy = self.maxSpeed
            self.images =self.imagesDown
        elif direction == "sleft":
            self.speedx = 0
        elif direction == "sright":
            self.speedx = 0
        elif direction == "sup":
            self.speedy = 0
        elif direction == "sdown":
            self.speedy = 0
            
            
            
    def ballCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                return True
        return False
