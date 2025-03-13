import pygame, sys,math,random
#e
class Bomb():
    def __init__(self, kind, startPos=[0,9]):
        if kind == "Bomb":
            self.image = pygame.image.load("Art/Objects/Bomb/Bomb.png")
            self.damage=1
        elif kind == "Bomb2x":
            self.image = pygame.image.load("Art/Objects/Bomb/Bomb2x.png")
            self.damage=2
        elif kind == "Bomb3x":
            self.image = pygame.image.load("Art/Objects/Bomb/Bomb3x.png")
            self.damage=3
        elif kind == "Bomb4x":
            self.image = pygame.image.load("Art/Objects/Bomb/Bomb4x.png")
            self.damage=4
        self.rect = self.image.get_rect(center=startPos)
        self.rad=self.rect.width/2
        
        self.kind = kind
        
        
        
        
        
    def collideSnake(self,other):
        if self != other:
            if self.rect.right>other.rect.left:
                if self.rect.left<other.rect.right:
                    if self.rect.bottom>other.rect.top:
                        if self.rect.top<other.rect.bottom:
                            if self.dist(other)<self.rad+other.rad:
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
                                
                                return True
        return False
                         
                         
                         
    
    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
        
        
    def respawn(self, size, tileSize):
        x =  random.randint(0, int(size[0]/tileSize)-1)*50+25
        y =  random.randint(1, int(size[1]/tileSize)-1)*50+25
        self.rect.center = [x,y]
        print(x,y)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
