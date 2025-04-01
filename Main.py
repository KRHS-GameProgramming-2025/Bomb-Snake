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
size = [1000,1000]
screen = pygame.display.set_mode(size)

mode="start"


while True:
    #-----------------------Start screen--------------------------------#
    if sound:
        pygame.mixer.music.load("Music/Background/Main_Theme.mp3")
        pygame.mixer.music.set_volume(.25)
        pygame.mixer.music.play()
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
        
    
    #-----------------------Mode Select Screen--------------------------#
    
    
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
        pygame.mixer.music.set_volume(.15)
        pygame.mixer.music.play()
    else:
        print("No Sound")

    counter = 0
    points = 0
    
    score = Hud ("Score: ", points, [0,0])
    playerSpeed=5
    player = Head(10,playerSpeed,[tileSize*10+tileSize/2,tileSize*9+tileSize/2])
    snake = [player]
    snakeSize = 3
    for i in range(snakeSize-1):
        snake += [Tail(snake[-1].maxSpeed, snake[-1].rect, snake[0].direction)]
    
    lives = player.lives
    life = Hud ("Lives: ", lives, [870,0])
          
    bombs = [Bomb("Bomb",[925,825])]
    bombDidSpawn=True
    bombSpawnRate=15
    
    bomb2xDidSpawn=True
    bomb2xSpawnRate=40
    
    bomb3xDidSpawn=True
    bomb3xSpawnRate=65
    
    bomb4xDidSpawn=True
    bomb4xSpawnRate=100
    frozen=False
    
    bomb5xDidSpawn=True
    bomb5xSpawnRate=110
    zap=False
    
    bomb6xDidSpawn=True
    bomb6xSpawnRate=123
    
    bmobDidSpawn=True
    bmobSpawnRate=51
    
    flameDidSpawn=True
    
    rockDidSpawn=True
    
    pitDidSpawn=True
    
    poisonDidSpawn=True
    
    goldbombDidSpawn=True
    goldbombSpawnRate=500
    
    
    bomb7xDidSpawn=True
    bomb7xSpawnRate=135
    sick=False
    
    bomb8xDidSpawn=True
    bomb8xSpawnRate=145

    bomb9xDidSpawn=True
    bomb9xSpawnRate=160
    clean=False
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
            
        if not bomb4xDidSpawn and points % bomb4xSpawnRate == 0:
            b = Bomb("Bomb4x",[625,525])
            b.respawn(size, tileSize)
            bombs+=[b]
            bomb4xDidSpawn=True
        elif bomb4xDidSpawn and points % bomb4xSpawnRate == 1:
            bomb4xDidSpawn=False
            
            
        if not bomb5xDidSpawn and points % bomb5xSpawnRate == 0:
            b = Bomb("Bomb5x",[625,525])
            b.respawn(size, tileSize)
            bombs+=[b]
            bomb5xDidSpawn=True
        elif bomb5xDidSpawn and points % bomb5xSpawnRate == 1:
            bomb5xDidSpawn=False
            
        if not bomb6xDidSpawn and points % bomb6xSpawnRate == 0:
            b = Bomb("Bomb6x",[625,525])
            b.respawn(size, tileSize)
            bombs+=[b]
            bomb6xDidSpawn=True
        elif bomb6xDidSpawn and points % bomb6xSpawnRate == 1:
            bomb6xDidSpawn=False
            
        if not bmobDidSpawn and points % bmobSpawnRate == 0:
            b = Bomb("bmoB",[625,525])
            b.respawn(size, tileSize)
            bombs+=[b]
            bmobDidSpawn=True
        elif bmobDidSpawn and points % bmobSpawnRate == 1:
            bmobDidSpawn=False
            
        if not goldbombDidSpawn and points % goldbombSpawnRate == 0:
            b = Bomb("goldBomb",[925,825])
            b.respawn(size, tileSize)
            bombs+=[b]
            goldbombDidSpawn=True
        elif goldbombDidSpawn and points % goldbombSpawnRate == 1:
            goldbombDidSpawn=False
        if not bomb7xDidSpawn and points % bomb7xSpawnRate == 0:
            b = Bomb("Bomb7x",[625,525])
            b.respawn(size, tileSize)
            bombs+=[b]
            bomb7xDidSpawn=True
        elif bomb7xDidSpawn and points % bomb7xSpawnRate == 1:
            bomb7xDidSpawn=False
        if not bomb8xDidSpawn and points % bomb8xSpawnRate == 0:
            b = Bomb("Bomb8x",[625,525])
            b.respawn(size, tileSize)
            bombs+=[b]
            bomb8xDidSpawn=True
        elif bomb8xDidSpawn and points % bomb8xSpawnRate == 1:
            bomb8xDidSpawn=False
            
        if not bomb9xDidSpawn and points % bomb9xSpawnRate == 0:
            b = Bomb("Bomb9x",[625,525])
            b.respawn(size, tileSize)
            bombs+=[b]
            bomb9xDidSpawn=True
        elif bomb9xDidSpawn and points % bomb9xSpawnRate == 1:
            bomb9xDidSpawn=False
      
        
        if not pelletDidSpawn and points % pelletSpawnRate == 0:
            p = Pellet([925,725])
            p.respawn(size, tileSize)
            pellets+=[p]
            pelletDidSpawn=True
        elif pelletDidSpawn and points % pelletSpawnRate == 1:
            pelletDidSpawn=False
                       
       
            
        for i, segment in enumerate(snake):
            segment.update(size)
            if segment.kind == "tail" and snake[i-1].didUpdate:
                segment.goKey(snake[i-1].prevDir, snake[i-1].turnCoor)
            
        
        for bomb in bombs:
            if player.collide(bomb):
                if bomb.kind =="Bomb4x":
                    playerSpeed=2.5
                    frozen=True
                if bomb.kind =="Bomb5x":
                    playerSpeed=20
                    zap=True
                if bomb.kind =="Bomb3x":
                    b = Bomb("flame",[625,525])
                    bombs+=[b]
                if bomb.kind =="Bomb6x":
                    b = Bomb("poison",[625,525])
                    bombs+=[b]
                if bomb.kind =="Bomb7x":
                    playerSpeed=1.25
                    sick=True
                if bomb.kind =="Bomb8x":
                    b = Bomb("rock",[625,525])
                    bombs+=[b]
                if bomb.kind =="Bomb8x":
                    b = Bomb("pit",[525,100])
                    bombs+=[b]
                if bomb.kind =="Bomb9x":
                    playerSpeed=10
                    clean=True
                    
                    
                bomb.snakeCollide(player)
                player.die(bomb.damage) # ~ bgImage=pygame.image.load("Art/Background/Mode_Select_idea.png")
    # ~ bgRect = bgImage.get_rect()
    # ~ while mode =="modeSelect":
        # ~ if event in pygame.event.get():
            # ~ if event.type:
                bomb.respawn(size, tileSize)
              
        
        for pellet in pellets:
            if player.collide(pellet):
                pellet.snakeCollide(player)
                points += 1
                score.update(points)
                pellet.respawn(size, tileSize)
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
            if frozen:
                frozen = False
                playerSpeed = 5
                
                
            if zap:
                zap = False
                playerSpeed = 5
              
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
        pygame.mixer.music.play()
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
        
