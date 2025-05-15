import pygame, sys,math,random, os

class Bomb():
    def __init__(self, kind, startPos=[0,9]):
        path = "Art/Objects/Bomb/"+ kind
        files = os.listdir(path)
        self.images = []
        for f in files:
            self.images += [pygame.image.load(path + "/"+ f)]
        self.frame = 0
        self.frameMax = len(self.images)-1
        self.animationTimer = 0
        self.animationTimerMax = int(60*1/len(self.images))
        self.image = self.images[self.frame]
    
        
        if kind == "Bomb":
            self.damage=1
        elif kind == "Bomb2x":
            self.damage=2
     
        elif kind == "Bomb4x":
            self.damage=4
        elif kind == "Bomb5x":
            self.damage=5
        elif kind == "Bomb7x":
            self.damage=7
        elif kind == "Bomb9x":
            self.damage=9
        elif kind == "bmoB":
            self.damage=-1
        elif kind == "x2bmoB":
            self.damage=-2
     
        else:
            print(kind)
        self.rect = self.image.get_rect(center=startPos)
        self.rad=self.rect.width/2
        self.kind = kind
        self.rad=self.rect.width/2
        self.kind = kind
        self.rad=self.rect.width/2
        
        self.kind = kind
        
        self.sound=pygame.mixer.Sound("Music/Objects/Bomb.wav")
        
        
    def collideSnake(self,other):
        if self != other:
            if self.rect.right>other.rect.left:
                if self.rect.left<other.rect.right:
                    if self.rect.bottom>other.rect.top:
                        if self.rect.top<other.rect.bottom:
                            if self.dist(other)<self.rad+other.rad:
                                return True
                                

                                
        return False
                    
    def explode(self):
        if self.animationTimer < self.animationTimerMax:
            self.animationTimer += 1
        else:
            self.animationTimer = 0
            if self.frame < self.frameMax:
                self.frame += 1
                self.image = self.images[self.frame]
            else:
                self.frame = 0
                self.image = self.images[self.frame]
                return True
        return False
                
        
    
    def dist(self,other):
        x1=self.rect.centerx
        y1=self.rect.centery
        x2=other.rect.centerx
        y2=other.rect.centery
        return math.sqrt((x2-x1)**2+(y2-y1)**2)
   
        
    def snakeCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                self.sound.play()
                                return True
        return False
    
    def collide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                return True
        return False
    
    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
        
    def respawn(self, size, tileSize):
        width = size[0]
        height = size[1]-150
        x =  random.randint(0, int(width/tileSize)-1)*50+25
        y =  random.randint(1, int(height/tileSize)-1)*50+25
        self.rect.center = [x,y]
        print(x,y)


