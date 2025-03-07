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
        clock.tick(60)
        
            


    #-----------------------Game screen--------------------------------
    if sound:
        pygame.mixer.music.load("Music/Background/Main_Background.mp3")
        pygame.mixer.music.set_volume(.25)
        pygame.mixer.music.play()
    else:
        print("No Sound")

    counter = 0
    points = 0
    
    score = Hud ("Score: ", points, [0,0])
    player = Head(3,5,[tileSize*10+tileSize/2,tileSize*9+tileSize/2])
    snake = [player]
    snake += [Tail(snake[-1].maxSpeed, snake[-1].rect, snake[-1].direction)]
    lives = player.lives
    life = Hud ("Lives: ", lives, [870,0])
          
    bombs = [Bomb("Bomb",[925,825])]
    bombDidSpawn=True
    bombSpawnRate=15
    
    bomb2xDidSpawn=True
    bomb2xSpawnRate=40
    
    bomb3xDidSpawn=True
    bomb3xSpawnRate=5
    
    pellets = [Pellet([925,725])]
    pelletDidSpawn=True
    pelletSpawnRate=15

    bgImage = pygame.image.load("Art/Background/board.png")
    bgRect = bgImage.get_rect()
    
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
            
        if not bombDidSpawn and points % bombSpawnRate == 0:
            b = Bomb("Bomb",[925,825])
            b.respawn(size, tileSize)
            bombs+=[b]
            bombDidSpawn=True
        elif bombDidSpawn and points % bombSpawnRate == 1:
            bombDidSpawn=False
            
        if not bomb2xDidSpawn and points % bomb2xSpawnRate == 0:
            b = Bomb("Bomb2x",[725,825])
            b.respawn(size, tileSize)
            bombs+=[b]
            bomb2xDidSpawn=True
        elif bomb2xDidSpawn and points % bomb2xSpawnRate == 1:
            bomb2xDidSpawn=False
            
        if not bomb3xDidSpawn and points % bomb3xSpawnRate == 0:
            b = Bomb("Bomb3x",[625,825])
            b.respawn(size, tileSize)
            bombs+=[b]
            bomb3xDidSpawn=True
        elif bomb3xDidSpawn and points % bomb3xSpawnRate == 1:
            bomb3xDidSpawn=False
         
        
        if not pelletDidSpawn and points % pelletSpawnRate == 0:
            p = Pellet([925,725])
            p.respawn(size, tileSize)
            pellets+=[p]
            pelletDidSpawn=True
        elif pelletDidSpawn and points % pelletSpawnRate == 1:
            pelletDidSpawn=False
                       
        
        for i, segment in enumerate(snake):
            if segment.update(size):
                break
            elif segment.kind == "tail" and snake[i-1].didUpdate:
                segment.goKey(snake[i-1].direction, snake[i-1].turnCoor)
            
        for bomb in bombs:
            if player.collide(bomb):
                player.die(bomb.damage)
                bomb.respawn(size, tileSize)
              
        
        for pellet in pellets:
            if player.collide(pellet):
                points += 1
                score.update(points)
                pellet.respawn(size, tileSize)

            
        
         
        if not player.living:
            lives=player.lives
            player = Head(player.lives,player.maxSpeed,[tileSize*10+tileSize/2,tileSize*9+tileSize/2])
            snake = [player]
            snake += [Tail(snake[-1].maxSpeed, snake[-1].rect, snake[-1].direction)]
            life.update(lives)
            if lives <=0:
                mode = "end"
        
        screen.blit(bgImage, bgRect)
        for bomb in bombs:
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
        
    #-----------------------End screen--------------------------------
    bgImage=pygame.image.load("Art/Background/dead_Screen.png")
    bgRect = bgImage.get_rect()
    while mode=="end":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                     mode="start"
            
        screen.blit(bgImage, bgRect)
        
        pygame.display.flip()
        clock.tick(60)
        
