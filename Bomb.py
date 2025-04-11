import pygame, sys,math,random

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
        elif kind == "Bomb5x":
            self.image = pygame.image.load("Art/Objects/Bomb/Bomb5x.png")
            self.damage=5
        elif kind == "Bomb6x":
            self.image = pygame.image.load("Art/Objects/Bomb/Bomb6x.png")
            self.damage=6
        elif kind == "bmoB":
            self.image = pygame.image.load("Art/Objects/Bomb/bmoB.png")
            self.damage=-1
        elif kind == "x2bmoB":
            self.image = pygame.image.load("Art/Objects/Bomb/x2bomB.png")
            self.damage=-2
        elif kind == "flame":
            self.image = pygame.image.load("Art/Objects/Bomb/flame.png")
            self.damage=1
        elif kind == "water":
            self.image = pygame.image.load("Art/Objects/Bomb/water.png")
            self.damage=3
        elif kind == "poison":
            self.image = pygame.image.load("Art/Objects/Bomb/poison.png")
            self.damage=2
        elif kind == "goldBomb":
            self.image = pygame.image.load("Art/Objects/Bomb/goldBomb.png")
            self.damage=100
        elif kind == "Bomb7x":
            self.image = pygame.image.load("Art/Objects/Bomb/Bomb7x.png")
            self.damage=7
        elif kind == "Bomb8x":
            self.image = pygame.image.load("Art/Objects/Bomb/Bomb8x.png")
            self.damage=8
        elif kind == "Bomb9x":
            self.image = pygame.image.load("Art/Objects/Bomb/Bomb9x.png")
            self.damage=9
        elif kind == "Bomb10x":
            self.image = pygame.image.load("Art/Objects/Bomb/Bomb10x.png")
            self.damage=10
        elif kind == "rock":
            self.image = pygame.image.load("Art/Objects/Bomb/rock.png")
            self.damage=3
        elif kind == "pit":
            self.image = pygame.image.load("Art/Objects/Bomb/pit.png")
            self.damage=3
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
        height = size[1]-100
        x =  random.randint(0, int(size[0]/tileSize)-1)*50+25
        y =  random.randint(1, int(size[1]/tileSize)-1)*50+25
        self.rect.center = [x,y]
        print(x,y)
        
        x =  random.randint(0, int(width/tileSize)-1)*50+25
        y =  random.randint(1, int(height/tileSize)-1)*50+25
        self.rect.center = [x,y]
        print(x,y)

