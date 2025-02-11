import pygame, sys, math, random
from Hud import *
from Pellet import *
from Head import *
from Bomb import *
from Tail import *
from Wall import *

pygame.init()
pygame.mixer.init()

if not pygame.font: print("Warning, fonts disabled")

size = [1000,900]
screen = pygame.display.set_mode(size)

pygame.mixer.music.load("Music/Background/Main_Background.mp3")
pygame.mixer.music.play()

clock = pygame.time.Clock();

tileSize = 50

score = Hud ("Score: ",[0,0])
player = Head(5,[tileSize*10+tileSize/2,tileSize*9+tileSize/2])
snake = [player]
snake += [Tail(snake[-1].maxSpeed, snake[-1].rect, snake[-1].direction)]
snake += [Tail(snake[-1].maxSpeed, snake[-1].rect, snake[-1].direction)]
snake += [Tail(snake[-1].maxSpeed, snake[-1].rect, snake[-1].direction)]
snake += [Tail(snake[-1].maxSpeed, snake[-1].rect, snake[-1].direction)]
      
bomb = Bomb([925,825])

bgImage = pygame.image.load("Art/Background/board.png")
bgRect = bgImage.get_rect()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame. K_a or event.key == pygame.K_LEFT:
                player.goKey("left")
            elif event.key == pygame. K_d or event.key == pygame.K_RIGHT:
                player.goKey("right")
            elif event.key == pygame. K_w or event.key == pygame.K_UP:
                player.goKey("up")
            elif event.key == pygame. K_s or event.key == pygame.K_DOWN:
                player.goKey("down")
        
                
                
                
    #for hittingPellet in pellets:
     #   for hitPellet in pellets:
      #    if hittingPellet.pelletCollide(hitPellet):
       #       if hittingPellet.kind == "player":
        #          pellets.remove(hitPellets)
         #         kills += 1
    for i, segment in enumerate(snake):
        segment.update(size)
        if segment.kind == "tail" and snake[i-1].didUpdate:
            segment.goKey(snake[i-1].direction, snake[i-1].turnCoor)
        
    

   # screen.fill([30,40,50])
    #for pellet in pellets:
     #   screen.blit(pellet.image, pellet.rect)
    screen.blit(bgImage, bgRect)
    screen.blit(score.image, score.rect)
    for segment in snake:
        screen.blit(segment.image, segment.rect)
    screen.blit(bomb.image, bomb.rect)
    pygame.display.flip()
    clock.tick(60)
    # print(clock.get_fps())
