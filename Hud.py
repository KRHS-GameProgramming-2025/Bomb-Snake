import pygame, sys, math

class Hud():
    def __init__ (self,baseText, startPos=[0,0]):
        self.font = pygame.font.Font(None, 46)
        self.baseText = baseText
        self.image = self.font.render("Score: 0", 1, (255,255,255))
        self.rect = self.image.get_rect(topleft = startPos)
        
        
        
    def update(self, score):
            text = self.baseText + str(score)
            self.image =  self.font.render(text, 1, (255,255,255))
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
            
            
