import pygame, sys,math

class Bomb():
    def __init__(self, startPos=[0,9]):
        self.image = pygame.image.load("Art/Objects/Bomb/Bomb.png")
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





    class enemy(object):
            
        def __init__(self, x, y, width, height, end):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.path = [self.x, self.end]
            self.vel = 3
            self.hitbox = (self.x + 17, self.y + 2, 31, 57) # NEW

        def draw(self,win):
            self.move()
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
    
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            self.hitbox = (self.x + 1, self.y + 1, 1, 1) # NEW
            pygame.draw.rect(win, (1,1,0), self.hitbox,2) # Draws the hit box around the enemy

        def move(self):
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0

    
    def hit(self):
        print("'hit'")
