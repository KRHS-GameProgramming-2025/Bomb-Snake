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

def checkSpawn(thing):
    for pellet in pellets:
        if thing.collide(pellet):
            return True
    for bomb in bombs:
        if thing.collide(bomb):
            return True
    for segment in snake:
        if thing.collide(segment):
            return True
            
    return False

clock = pygame.time.Clock();

if not pygame.font: print("Warning, fonts disabled")
tileSize = 50
size = [1000,1000]
screen = pygame.display.set_mode(size)

mode="start"


while True:
    #-----------------------Start screen--------------------------------#
    if sound:
        pygame.mixer.music.load("Music/Background/Main_Theme.mp3")
        pygame.mixer.music.set_volume(.25)
        pygame.mixer.music.play(0)
    else:
        print("No Sound")
    
    bgImage=pygame.image.load("Art/Background/Start_Screen.png")
    bgRect = bgImage.get_rect()
    while mode=="start":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                     mode="play"
                if event.key == pygame.K_m:
                    mode="modeSelect"
                if event.key == pygame.K_c:
                    mode="credits"
            
        screen.blit(bgImage, bgRect)
        

        
        pygame.display.flip()
        clock.tick(60)
        
    
    #-----------------------Credits Screen------------------------------#
    if sound:
        pygame.mixer.music.load("Music/Background/Thanks!.mp3")
        pygame.mixer.music.set_volume(.25)
        pygame.mixer.music.play(0)
    else:
        print("No Sound")
    
    bgImage=pygame.image.load("Art/Background/Credit_idea.png")
    bgRect = bgImage.get_rect()
    while mode =="credits":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                     mode="play"
                     
        screen.blit(bgImage, bgRect)
        
        pygame.display.flip()
        clock.tick(60)

    #-----------------------Credits Screen------------------------------#
    if sound:
        pygame.mixer.music.load("Music/Background/CHOOSE.mp3")
        pygame.mixer.music.set_volume(.25)
        pygame.mixer.music.play(0)
    else:
        print("No Sound")
    
    bgImage=pygame.image.load("Art/Background/Mode_Select_idea.png")
    bgRect = bgImage.get_rect()
    while mode =="modeSelect":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                     mode="play"
                     
        screen.blit(bgImage, bgRect)
        
        pygame.display.flip()
        clock.tick(60)




    #-----------------------Game screen---------------------------------#
    if sound:
        pygame.mixer.music.load("Music/Background/Main_Background.mp3")
        pygame.mixer.music.set_volume(.25)
        pygame.mixer.music.play(0)
    else:
        print("No Sound")

    counter = 0
    points = 0
    
    score = Hud ("Score: ", points, [70,938])
    playerSpeed=5
    player = Head(10,playerSpeed,[tileSize*10+tileSize/2,tileSize*9+tileSize/2])
    snake = [player]
    snakeSize = 3
    for i in range(snakeSize-1):
        snake += [Tail(snake[-1].maxSpeed, snake[-1].rect, snake[0].direction)]
    
    lives = player.lives
    life = Hud ("Lives: ", lives, [765,938])
          
    bombs = [Bomb("Bomb",[550,425])]
    
    bombSpawnRates={"Bomb": 1,
                    "Bomb2x": 5,
                    "Bomb3x": 10,
                    "Bomb4x": 15,
                    "Bomb5x": 20,
                    "Bomb6x": 25,
                    "bmoB": 30,
                    "x2bmoB": 35,
                    "goldBomb": 40,
                    "Bomb7x": 45,
                    "Bomb8x": 50,
                    "Bomb9x": 55,
                    "Bomb10x": 60
                    }
                    
    bombDidSpawns={"Bomb": True,
                   "Bomb2x": True,
                   "Bomb3x": True,
                   "Bomb4x": True,
                   "Bomb5x": True,
                   "Bomb6x": True,
                   "bmoB": True,
                   "x2bmoB": True,
                   "goldBomb": True,
                   "Bomb7x": True,
                   "Bomb8x": True,
                   "Bomb9x": True,
                   "Bomb10x": True
                    }
    
    bombDidSpawn=True
    bombSpawnRate=1
    
    bomb2xDidSpawn=True
    bomb2xSpawnRate=1
    
    bomb3xDidSpawn=True
    bomb3xSpawnRate=1
    
    bomb4xDidSpawn=True
    bomb4xSpawnRate=1
    
    bomb5xDidSpawn=True
    bomb5xSpawnRate=1
    
    bomb6xDidSpawn=True
    bomb6xSpawnRate=1
    
    bmobDidSpawn=True
    bmobSpawnRate=1
    
    x2bmobDidSpawn=True
    x2bmobSpawnRate=1
    
    
    goldbombDidSpawn=True
    goldbombSpawnRate=1
    
    
    bomb7xDidSpawn=True
    bomb7xSpawnRate=1

    
    bomb8xDidSpawn=True
    bomb8xSpawnRate=1

    bomb9xDidSpawn=True
    bomb9xSpawnRate=1

    
    bomb10xDidSpawn=True
    bomb10xSpawnRate=185
    
    pellets = [Pellet([550,425])]
    pelletDidSpawn=True
    pelletSpawnRate=15

    bgImage = pygame.image.load("Art/Background/board.png")
    bgRect = bgImage.get_rect()
    Bomb
    didSpawn=True

    while mode=="play":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame. K_a or event.key == pygame.K_LEFT:
                    if player.direction != "right":
                        player.goKey("left")
                elif event.key == pygame. K_d or event.key == pygame.K_RIGHT:
                    if player.direction != "left":
                        player.goKey("right")
                elif event.key == pygame. K_w or event.key == pygame.K_UP:
                    if player.direction != "down":
                        player.goKey("up")
                elif event.key == pygame. K_s or event.key == pygame.K_DOWN:
                    if player.direction != "up":
                        player.goKey("down")
        
        
        for bomb in bombSpawnRates.keys():
            if not bombDidSpawns[bomb] and points % bombSpawnRates[bomb] == 0:
                b = Bomb(bomb,[925,825])
                b.respawn(size, tileSize)
                if checkSpawn(b):
                    break
                else:
                    bombs+=[b] 
                    bombDidSpawns[bomb]=True
            elif bombDidSpawns[bomb] and points % bombSpawnRates[bomb] == 1:
                bombDidSpawns[bomb]=False
            
        
      
        
        if not pelletDidSpawn and points % pelletSpawnRate == 0:
            p = Pellet([925,725])
            p.respawn(size, tileSize)
            pellets+=[p]
            print(checkSpawn(pellets[-1]))
            if checkSpawn(pellets[-1]):
                pellets.remove(pellets[-1])
            else:
                pelletDidSpawn=True
        elif pelletDidSpawn and points % pelletSpawnRate == 1:
            pelletDidSpawn=False
   
        
        

            
        for i, segment in enumerate(snake):
            segment.update(size)
            if segment.kind == "tail" and snake[i-1].didUpdate:
                segment.goKey(snake[i-1].prevDir, snake[i-1].turnCoor)
            
        
        for bomb in bombs:
            if player.collide(bomb):
                bomb.snakeCollide(player)
                player.die(bomb.damage) 
                bomb.respawn(size, tileSize)
              
        
        for pellet in pellets:
            if player.collide(pellet):
                pellet.snakeCollide(player)
                points += 1
                score.update(points)
                
                goodSpawn = False
                while not goodSpawn:
                    print("Respawning")
                    pellet.respawn(size, tileSize)
                    goodSpawn = not checkSpawn(pellet)
                print("-----")
                
                snake += [Tail(snake[-1].maxSpeed, snake[-1].rect, snake[-1].prevDir)]
                
                
        for i, segment, in enumerate(snake):        
            if i >=4 and player.collide(segment):
                player.die()

            
        
         
        if not player.living:
            lives=player.lives
            player = Head(player.lives,playerSpeed,[tileSize*10+tileSize/2,tileSize*9+tileSize/2])
            snake = [player]
            for i in range(snakeSize-1):
                snake += [Tail(snake[-1].maxSpeed, snake[-1].rect, snake[0].direction)]
              
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
        
    #-----------------------End screen----------------------------------#
    if sound:
        pygame.mixer.music.load("Music/Background/DEATH.mp3")
        pygame.mixer.music.set_volume(.25)
        pygame.mixer.music.play(0)
    else:
        print("No Sound")
    
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
        
