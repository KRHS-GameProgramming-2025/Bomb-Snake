import pygame,math, sys, random


class Tail():
    def __init__(self, maxSpeed, headRect, headDir):
        self.tileSize = 50
        self.imagesUpDown = [pygame.image.load("Art/Snake/snake_Body_Down and Up.PNG")]
        self.imagesLeftRight = [pygame.image.load("Art/Snake/snake_Body_Left and Right.PNG")]
        self.images = self.imagesUpDown

        self.frame = 0
        self.frameMax = len(self.images)-1
        self.image = self.images[self.frame]
        if headDir[-2:] == "up":
            startPos = [headRect.centerx, headRect.centery+self.tileSize]
        elif headDir[-2:] == "up":
            startPos = [headRect.centerx, headRect.centery+self.tileSize]    
            
        self.rect = self.image.get_rect(center = startPos)
        
        self.speedx = 0
        self.speedy = -maxSpeed
        self.speed = [self.speedx, self.speedy]
        self.rad = (self.rect.height/2 + self.rect.width/2)/2
        self.direction = headDir
        self.prevDir = headDir
        
        self.maxSpeed = maxSpeed
        self.kind = "tail"
        
        self.animationTimer = 0
        self.animationTimerMax = 60/10
        
        self.targetCoor = []
        self.turnCoor = self.rect.center
        self.didUpdate = False
        self.keyLock = False
         
        
        
    def update(self, size):
        self.didUpdate = False
        self.move()
        self.animationTimer += 1
        self.animate()
        self.wallCollide(size)

    def goKey(self, direction, turnCoor):
        if not self.keyLock:
            self.prevDir = self.direction
            self.direction = direction
            self.targetCoor = turnCoor
            self.keyLock = True
        

    
    def upDateDirection(self):
        if self.direction == "left":
            self.speedx = -self.maxSpeed
            self.speedy = 0
            self.images =self.imagesLeftRight
        elif self.direction == "right":
            self.speedx = self.maxSpeed
            self.speedy = 0
            self.images =self.imagesLeftRight
        elif self.direction == "up":
            self.speedx = 0
            self.speedy = -self.maxSpeed
            self.images =self.imagesUpDown
        elif self.direction == "down":
            self.speedx = 0
            self.speedy = self.maxSpeed
            self.images =self.imagesUpDown
            
        # ~ if self.prevDir != self.direction:
            # ~ if self.prevDir == "up":
                # ~ if self.direction == "right":
                    # ~ self.rect = self.rect.move([-self.tileSize, -self.tileSize])
                # ~ if self.direction == "left":
                    # ~ self.rect = self.rect.move([self.tileSize, -self.tileSize])
                # ~ if self.direction == "down":
                    # ~ self.rect = self.rect.move([0, -self.tileSize*2])
            # ~ if self.prevDir == "right":
                # ~ if self.direction == "up":
                    # ~ self.rect = self.rect.move([-self.tileSize, -self.tileSize])
                # ~ if self.direction == "left":
                    # ~ self.rect = self.rect.move([self.tileSize, -self.tileSize])
                # ~ if self.direction == "down":
                    # ~ self.rect = self.rect.move([0, -self.tileSize*2])
            
        
            
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed) 
        if self.rect.center == self.targetCoor:
            self.upDateDirection()
            self.turnCoor = self.rect.center
            self.didUpdate = True
            self.keyLock = False
    
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
            
        
    def animate(self):
        if self.animationTimer >=self.animationTimerMax:
            self.animationTimer = 0
            if self.frame >= self.frameMax:
                self.frame = 0
            else:
                self.frame += 1
            self.image = self.images[self.frame]
        
