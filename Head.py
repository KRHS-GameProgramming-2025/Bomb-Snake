import pygame, sys, math


class Head():
    def __init__(self, maxSpeed=5, startPos=[0,0]):
        self.tileSize = 50
        
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
        self.direction = "up"
        self.prevDir = "sup"
        
        self.maxSpeed = maxSpeed
        self.kind = "head"
        
        self.animationTimer = 0
        self.animationTimerMax = 60/10
        
        self.living = True
        self.didUpdate = False
        
    def update(self, size):
        self.didUpdate = False
        self.move()
        self.wallCollide(size)
        self.animationTimer += 1
        self.animate()

    def goKey(self, direction):
        self.prevDir = self.direction
        self.direction = direction
        
    
    def upDateDirection(self):
        print("........................")
        if self.direction == "left":
            self.speedx = -self.maxSpeed
            self.speedy = 0
            self.images =self.imagesLeft
        elif self.direction == "right":
            self.speedx = self.maxSpeed
            self.speedy = 0
            self.images =self.imagesRight
        elif self.direction == "up":
            self.speedx = 0
            self.speedy = -self.maxSpeed
            self.images =self.imagesUp
        elif self.direction == "down":
            self.speedx = 0
            self.speedy = self.maxSpeed
            self.images =self.imagesDown
        self.didUpdate = True
        
            
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed) 
        if (self.rect.centerx-self.tileSize/2)%50 == 0 and (self.rect.centery-self.tileSize/2)%50==0:
            self.upDateDirection()
        
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
            self.rect.centery = self.tileSize/2
        if self.rect.top < 0: 
            self.rect.centery = height-self.tileSize/2
        if self.rect.right > width:
            self.rect.centerx = self.tileSize/2
        if self.rect.left < 0:
            self.rect.centerx = width-self.tileSize/2
            
    def pelletCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                return True
        return False
