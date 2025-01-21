import pygame, sys, math


class Head():
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        self.imagesRight = [pygame.image.load("Art/Snake/snake_head_right.PNG")]
        self.imagesDown = [pygame.image.load("Art/Snake/snake_head_down.PNG")]
        self.imagesLeft = [pygame.image.load("Art/Snake/snake_head_left.PNG")]
        self.imagesUp = [pygame.image.load("Art/Snake/snake_head_up.PNG")]
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
        
        self.animationTimer = 0
        self.animationTimerMax = 60/10
        
        self.living = True
        
    def update(self, size):
        self.move()
        self.wallCollide(size)
        self.animationTimer += 1
        self.animate()

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
            
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)  
        
    def animate(self):
        if self.animationTimer >=self.animationTimerMax:
            self.animationTimer = 0
            if self.frame >= self.frameMax:
                self.frame = 0
            else:
                self.frame += 1
            self.image = self.images[self.frame]
        
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if self.rect.bottom >  height: 
            self.living = False
        if self.rect.top < 0: 
            self.living = False
        if self.rect.right > width:
            self.living = False
        if self.rect.left < 0:
            self.living = False
            
    def pelletCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                return True
        return False
