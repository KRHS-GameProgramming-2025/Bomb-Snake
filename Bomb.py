import pygame, sys,math

class Bomb():
    def __init__(self, startPos=[0,0]):
        self.image = pygame.image.load("Art/Objects/Bomb.png")
        self.rect = self.image.get_rect(center=startPos)
        self.rad=self.rect.width/2
        
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
