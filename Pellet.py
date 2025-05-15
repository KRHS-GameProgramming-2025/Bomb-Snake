import pygame, sys, math, random

class Pellet():
    def __init__(self, startPos=[0,5]):
        self.fruits=[
            "mango", "blueberries", "dragonfruit","pomegrante", "B3RR0R","spaghetti"]
        self.fruitOdds = [
              20   ,    50        ,    19        ,   10       ,    5  ,   1  ]
        self.totalFruitOdds = 0
        for fo in self.fruitOdds:
            self.totalFruitOdds += fo
        fruitValue = random.randint(0,self.totalFruitOdds)
        print(fruitValue)
        index = 0
        for i, fo in enumerate(self.fruitOdds):
            fruitValue -= fo
            if fruitValue <= 0:
                index = i
                break
        self.fruit=self.fruits[index]
        self.image = pygame.image.load("Art/Objects/"+self.fruit+".png")
        self.rect = self.image.get_rect(center=startPos)
        self.rad=self.rect.width/2
        
        self.kind = "pellet"
        
        self.sound=pygame.mixer.Sound("Music/Objects/fruit.wav")
        
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
        height = size[1]-200
        fruitValue = random.randint(0,self.totalFruitOdds)
        index = 0
        for i, fo in enumerate(self.fruitOdds):
            fruitValue -= fo
            if fruitValue <= 0:
                index = i
                break
        self.fruit=self.fruits[index]
        self.image = pygame.image.load("Art/Objects/"+self.fruit+".png")
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rad=self.rect.width/2
        
        x =  random.randint(0, int(width/tileSize)-1)*50+25
        y =  random.randint(1, int(height/tileSize)-1)*50+25
        self.rect.center = [x,y]
