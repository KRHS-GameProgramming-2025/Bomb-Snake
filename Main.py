import pygame, sys, math, random
from Hud import *
from Pellet import *
from Head import *
from Bomb import *
from Tail import *
from Wall import *
pygame.init()
pygame.mixer.init()

try:
    pygame.mixer.init()
    sound = True
except:
    sound = False

clock = pygame.time.Clock();

if not pygame.font: print("Warning, fonts disabled")
tileSize = 50
size = [1000,900]
screen = pygame.display.set_mode(size)

mode="start"

while True:
    #-----------------------Start screen--------------------------------
    bgImage=pygame.image.load("Art/Background/Start_Screen.png")
    bgRect = bgImage.get_rect()
    while mode=="start":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                     mode="play"
            
        screen.blit(bgImage, bgRect)
        
        pygame.display.flip()
        clock.tick(70)


    #-----------------------Start screen--------------------------------
    if sound:
        pygame.mixer.music.load("Music/Background/Main_Background.mp3")
        pygame.mixer.music.set_volume(.25)
        pygame.mixer.music.play()
    else:
        print("No Sound")

    counter = 0;
    score = Hud ("Score: ",[0,0])
    player = Head(5,[tileSize*10+tileSize/2,tileSize*9+tileSize/2])
    snake = [player]
    snake += [Tail(snake[-1].maxSpeed, snake[-1].rect, snake[-1].direction)]
    life = Hud ("Lives: ", [870,0])
          
    bomb = Bomb([925,825])
    pellets = [Pellet([925,725])]

    kills = 0

    bgImage = pygame.image.load("Art/Background/board.png")
    bgRect = bgImage.get_rect()
    points = 0
    didSpawn=True

    while mode=="play":
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
            
        if not didSpawn and points%20==0:
	        p = Pellet([925,725])
	        p.respawn(size, tileSize)
	        pellets+=[p]
	        didSpawn=True
	    elif didSpawn and points%20==1:
	        didSpawn=False
	                   
	   
	    if not didSpawn and points%15==0:
	        b = Bomb([925,825])
	        b.respawn(size, tileSize)
	        bomb+=[b]
	        didSpawn=True
	    elif didSpawn and points%15==1:
	        didSpawn=False
        
        for i, segment in enumerate(snake):
            segment.update(size)
            if segment.kind == "tail" and snake[i-1].didUpdate:
                segment.goKey(snake[i-1].direction, snake[i-1].turnCoor)
            
        if player.collide(bomb):
            print("Boom")
            bomb.respawn(size, tileSize)
        for pellet in pellets:
            if player.collide(pellet):
                points += 1
                score.update(points)
                pellet.respawn(size, tileSize)
            
      #  if player.wallCollide:
       #     print(".")
            
        
        screen.blit(bgImage, bgRect)
        screen.blit(bomb.image, bomb.rect)
        for pellet in pellets:
            screen.blit(pellet.image, pellet.rect)
        for segment in snake:
            screen.blit(segment.image, segment.rect)
        screen.blit(score.image, score.rect)
        screen.blit(life.image, life.rect)
        pygame.display.flip()
        clock.tick(60)
        # print(clock.get_fps())
