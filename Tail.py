import pygame,math, sys, random


class Tail():
    def __init__(self, maxSpeed, headRect, headDir):
        self.tileSize = 50
        self.imagesUp = [pygame.image.load("Art/Snake/snake_Body_Down and Up.PNG")]
        self.imagesRight = [pygame.image.load("Art/Snake/snake_Body_Left and Right.PNG")]
        self.images = self.imagesUp

        self.frame = 0
        self.frameMax = len(self.images)-1
        self.image = self.images[self.frame]
        if headDir[-2:] == "up":
            startPos = [headRect.centerx, headRect.centery+self.tileSize]
        if headDir[-2:] == "up":
            startPos = [headRect.centerx, headRect.centery+self.tileSize]    
            
        self.rect = self.image.get_rect(center = startPos)
        
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.rad = (self.rect.height/2 + self.rect.width/2)/2
        self.direction = headDir
        self.prevDir = headDir
        
        self.maxSpeed = maxSpeed
        self.kind = "tail"
        
        self.animationTimer = 0
        self.animationTimerMax = 60/10
        
        
        
    def update(self, size):
        print(self.kind, self.direction)
        self.prevDir = self.direction
        self.move()
        self.animationTimer += 1
        self.animate()

    def goKey(self, direction):
        self.prevDir = self.direction
        self.direction = direction
        if self.direction == "left":
            self.speedx = -self.maxSpeed
        elif self.direction == "right":
            self.speedx = self.maxSpeed
            self.images =self.imagesRight
        elif self.direction == "up":
            self.speedy = -self.maxSpeed
            self.images =self.imagesUp
        elif self.direction == "down":
            self.speedy = self.maxSpeed
        elif self.direction == "sleft":
            self.speedx = 0
        elif self.direction == "sright":
            self.speedx = 0
        elif self.direction == "sup":
            self.speedy = 0
        elif self.direction == "sdown":
            self.speedy = 0
            
        if self.prevDir != self.direction and self.direction[0] != 's':
            if self.prevDir[-2:] == "up":
                if self.direction == "right":
                    self.rect = self.rect.move([-self.tileSize, -self.tileSize])
                if self.direction == "left":
                    self.rect = self.rect.move([self.tileSize, -self.tileSize])
                if self.direction == "down":
                    self.rect = self.rect.move([0, -self.tileSize*2])
            if self.prevDir[-2:] == "right":
                if self.direction == "up":
                    self.rect = self.rect.move([-self.tileSize, -self.tileSize])
                if self.direction == "left":
                    self.rect = self.rect.move([self.tileSize, -self.tileSize])
                if self.direction == "down":
                    self.rect = self.rect.move([0, -self.tileSize*2])
            
                    
            
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
        
