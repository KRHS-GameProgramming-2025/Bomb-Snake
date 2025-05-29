import pygame, sys, math, random
from Hud import *
from Pellet import *
from Head import *
from Bomb import *
from Tail import *
from Button import*
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
clicked = False
dificulty = "Normal"

cPressed = False
hPressed = False
gPressed = False
chg = False



while True:
    #-----------------------Start screen--------------------------------#
    if sound:
        pygame.mixer.music.load("Music/Background/Main_Theme.mp3")
        pygame.mixer.music.set_volume(.25)
        pygame.mixer.music.play(loops=-1)
    else:
        print("No Sound")
        
    pygame.mouse.set_visible(True)
    
    buttons = [Button("Start", [191,325], 1), 
               Button("Modes", [191,425], 1),
               Button("Credits", [191,525], 1),
               Button("Bombs", [191,625], 1)]
    
    bgImage=pygame.image.load("Art/Background/Start_Screen.png")
    bgRect = bgImage.get_rect()
    while mode=="start":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                     mode="play"
                elif event.key == pygame.K_c and not cPressed and not hPressed and not gPressed:
                    cPressed = True
                elif event.key == pygame.K_h and cPressed and not hPressed and not gPressed:
                    hPressed = True
                elif event.key == pygame.K_g and cPressed and hPressed and not gPressed:
                    gPressed = True
                    
                else:
                    cPressed = False
                    hPressed = False
                    gPressed = False
                    
        if cPressed and hPressed and gPressed:
            print("CHG")
        elif event.type == pygame.MOUSEMOTION:
           for button in buttons:
               button.collidePoint(event.pos, clicked) 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked = True
                for button in buttons:
                    button.collidePoint(event.pos, clicked)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicked = False
                for button in buttons:
                    if button.collidePoint(event.pos, clicked):
                        if button.name == "Start":
                            mode="play"
                        elif button.name == "Modes":
                            mode="modeSelect"
                        elif button.name == "Credits":
                            mode="credits"
                        elif button.name == "Bombs":
                            mode="bomb"
            
        screen.blit(bgImage, bgRect)
        
        for button in buttons:
            screen.blit(button.image, button.rect)
        

        
        pygame.display.flip()
        clock.tick(60)
        
    
    #-----------------------Credits Screen------------------------------#
    if sound:
        pygame.mixer.music.load("Music/Background/Thanks!.mp3")
        pygame.mixer.music.set_volume(.25)
        pygame.mixer.music.play(-1)
    else:
        print("No Sound")
        
    pygame.mouse.set_visible(True)
        
    buttons = [Button("BACK", [840,950], 1),
               Button ("PLAY", [160,950], 1)]

    
    bgImage=pygame.image.load("Art/Background/Credit_idea.png")
    bgRect = bgImage.get_rect()
    while mode =="credits":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                     mode="play"
                     
            elif event.type == pygame.MOUSEMOTION:
               for button in buttons:
                   button.collidePoint(event.pos, clicked) 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                    for button in buttons:
                        button.collidePoint(event.pos, clicked)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = False
                    for button in buttons:
                        if button.collidePoint(event.pos, clicked):
                            if button.name == "BACK":
                                mode="start"
                            elif button.name == "PLAY":
                                mode="play"
                     
        screen.blit(bgImage, bgRect)
        
        for button in buttons:
            screen.blit(button.image, button.rect)
        
        pygame.display.flip()
        clock.tick(60)

    #-----------------------Modes Screen--------------------------------#
    if sound:
        pygame.mixer.music.load("Music/Background/CHOOSE.mp3")
        pygame.mixer.music.set_volume(.25)
        pygame.mixer.music.play(-1)
    else:
        print("No Sound")
        
    pygame.mouse.set_visible(True)
        
    buttons = [Button("BACK", [500,950], 1),
               Button ("Easy", [160,350], 1),
               Button ("Normal", [500,350], 1),
               Button ("Hard", [840,350], 1),
               Button ("Elemental", [500,450], 1)]
    
    bgImage=pygame.image.load("Art/Background/Mode_Select_idea.png")
    bgRect = bgImage.get_rect()
    while mode =="modeSelect":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                     mode="play"
                elif event.key == pygame.K_c and not cPressed and not hPressed and not gPressed:
                        cPressed = True
                elif event.key == pygame.K_h and cPressed and not hPressed and not gPressed:
                        hPressed = True
                elif event.key == pygame.K_g and cPressed and hPressed and not gPressed:
                        gPressed = True
                        
                else:
                    cPressed = False
                    hPressed = False
                    gPressed = False
                        
        if cPressed and hPressed and gPressed:
            print("CHG")
            if not chg: buttons+=[Button("CHG",[840,450],1)]
            chg = True
            cPressed = False
            hPressed = False
            gPressed = False
                     
        elif event.type == pygame.MOUSEMOTION:
           for button in buttons:
               button.collidePoint(event.pos, clicked) 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked = True
                for button in buttons:
                    button.collidePoint(event.pos, clicked)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicked = False
                for button in buttons:
                    if button.collidePoint(event.pos, clicked):
                        if button.name == "BACK":
                            mode="start"
                        else:
                            dificulty = button.name
                            mode = "play"
                                
                     
        screen.blit(bgImage, bgRect)
        
        for button in buttons:
            screen.blit(button.image, button.rect)
                    
        
        pygame.display.flip()
        clock.tick(60)


    #-----------------------Bomb Screen---------------------------------#
    if sound:
        pygame.mixer.music.load("Music/Background/KaBOOM.mp3")
        pygame.mixer.music.set_volume(.25)
        pygame.mixer.music.play(-1)
    else:
        print("No Sound")
        
    pygame.mouse.set_visible(True)
        
    buttons = [Button("BACK", [840,950], 1),
               Button ("PLAY", [160,950], 1)]
    
    bgImage=pygame.image.load("Art/Background/Bomb_Screen.png")
    bgRect = bgImage.get_rect()
    while mode =="bomb":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                     mode="play"
                     
            elif event.type == pygame.MOUSEMOTION:
               for button in buttons:
                   button.collidePoint(event.pos, clicked) 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                    for button in buttons:
                        button.collidePoint(event.pos, clicked)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = False
                    for button in buttons:
                        if button.collidePoint(event.pos, clicked):
                            if button.name == "BACK":
                                mode="start"
                            elif button.name == "PLAY":
                                mode="play"
                     
        screen.blit(bgImage, bgRect)
        
        for button in buttons:
            screen.blit(button.image, button.rect)
                    

        
        pygame.display.flip()
        clock.tick(60)




    #-----------------------Game screen---------------------------------#
    if sound:
        pygame.mixer.music.load("Music/Background/Main_Background.mp3")
        pygame.mixer.music.set_volume(.25)
        pygame.mixer.music.play(loops=-1)
    else:
        print("No Sound")
        
    pygame.mouse.set_visible(False)

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
          
    
    
    if dificulty == "Normal":
        bombs = [Bomb("Bomb",[550,425])]
        bombs[-1].respawn(size, tileSize)
      
        bombSpawnRates={"Bomb": 15,
                        "Bomb2x": 25,
                        "Bomb3x": 35,
                        "Bomb4x": 45,
                        "Bomb1+":52 ,
                        "Bomb2+": 54 }
                        
        bombDidSpawns={"Bomb": True,
                       "Bomb2x": True,
                       "Bomb3x": True,
                       "Bomb4x": True,
                       "Bomb2+": True,
                       "Bomb1+": True }
    elif dificulty == "Easy":
        bombs = []
        bombSpawnRates={}
        bombDidSpawns={}

    elif dificulty == "Hard":
        bombs = [Bomb("Bomb",[550,425])]
        bombs[-1].respawn(size, tileSize)
    
        bombSpawnRates={"Bomb": 15,
                        "Bomb2x": 25,
                        "Bomb3x": 35,
                        "Bomb4x": 45,
                        "Bomb5x": 55,
                        "Bomb7x": 75,
                        "Bomb9x": 95,
                        "Bomb10x": 105,
                        "Bomb1+":52 ,
                        "Bomb2+": 54 }
                        
        bombDidSpawns={"Bomb": True,
                       "Bomb2x": True,
                       "Bomb3x": True,
                       "Bomb4x": True,
                       "Bomb5x": True,
                       "Bomb7x": True,
                       "Bomb9x": True,
                       "Bomb10x": True,
                       "Bomb1+": True,
                       "Bomb2+": True }
        
    elif dificulty == "Elemental":
        bombs = [Bomb("Bomb",[550,425])]
        bombs[-1].respawn(size, tileSize)
        frozen=False
        zap=False
        sick=False
        clean=False
       
        bombSpawnRates={"Bomb4x": 45,
                        "Bomb5x": 55,
                        "Bomb9x": 95,
                        "Bomb10x": 105,
                        "Bomb1+":52 ,
                        "Bomb2+": 54 }

                        
        bombDidSpawns={"Bomb3x": True,
                        "Bomb4x": True,
                       "Bomb5x": True,
                        "Bomb9x": True,
                        "Bomb10x": True,
                       "Bomb1+": True,
                       "Bomb2+": True }
                       
    elif dificulty == "CHG":
        bombs = [Bomb("Bomb",[550,425])]
        bombs[-1].respawn(size, tileSize)
        if sound:
            pygame.mixer.music.load("Music/Background/CHG.mp3")
            pygame.mixer.music.set_volume(.25)
            pygame.mixer.music.play(loops=-1)
        else:
            print("No Sound")
        
        bombSpawnRates={"Bomb": 15,
                        "Bomb2x": 25,
                        "Bomb3x": 45,
                        "Bomb4x": 50,
                        "Bomb5x": 55,
                        "Bomb6x": 65,
                        "Bomb7x": 75,
                        "Bomb8x": 80,
                        "Bomb9x": 85,
                        "Bomb10x": 90}
                        
        bombDidSpawns={"Bomb": True,
                       "Bomb2x": True,
                       "Bomb3x": True,
                       "Bomb4x": True,
                       "Bomb5x": True,
                       "Bomb6x": True,
                       "Bomb7x": True,
                       "Bomb8x": True,
                       "Bomb9x": True,
                       "Bomb10x": True}
    
    pellets = [Pellet([550,425])]
    pellets[-1].respawn(size, tileSize)
    pelletDidSpawn=True
    pelletSpawnRate=15

    bgImage = pygame.image.load("Art/Background/board.png")
    bgRect = bgImage.get_rect()
    
    didSpawn=True
    frozen=False
    zap=False
    sick=False
    clean=False
    bombIsExploding = False
    theBomb=None

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
        
        if bombIsExploding:
            if theBomb.explode():
                bombIsExploding = False
                
                goodSpawn = False
                while not goodSpawn:
                    print("Respawning")
                    theBomb.respawn(size, tileSize)
                    goodSpawn = not checkSpawn(bomb)
                player.die(theBomb.damage)
                print("die")
                theBomb=None
        
        else:
        
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
             
            if not player.living:
                lives=player.lives
                if frozen:
                    frozen=False
                elif zap:
                    zap=False
                elif sick:
                    sick=False
                elif clean:
                    clean=False
                else:
                    playerSpeed = 5
                player = Head(player.lives,playerSpeed,[tileSize*10+tileSize/2,tileSize*9+tileSize/2])
                snake = [player]
                for i in range(snakeSize-1):
                    snake += [Tail(snake[-1].maxSpeed, snake[-1].rect, snake[0].direction)]
                
                life.update(lives)
                
                if lives <=0:
                    mode = "end"
                    
            if points >=360:
                mode = "end"
            
          
            
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
                if player.collide(bomb) and not bombIsExploding:
                    bomb.snakeCollide(player)
                    bombIsExploding = True
                    
                    if bomb.kind =="Bomb4x":
                        playerSpeed=2.5
                        frozen=True
                    elif bomb.kind =="Bomb5x":
                        playerSpeed=12.5
                        zap=True
                    elif bomb.kind =="Bomb7x":
                        playerSpeed=1.25
                        sick=True
                    elif bomb.kind =="Bomb9x":
                        playerSpeed=10
                        clean=True
                    theBomb=bomb
                    bomb=None
                    break
            
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
                if frozen:
                    frozen=False
                elif zap:
                    zap=False
                elif sick:
                    sick=False
                elif clean:
                    clean=False
                else:
                    playerSpeed = 5
                player = Head(player.lives,playerSpeed,[tileSize*10+tileSize/2,tileSize*9+tileSize/2])
                snake = [player]
                for i in range(snakeSize-1):
                    snake += [Tail(snake[-1].maxSpeed, snake[-1].rect, snake[0].direction)]
                
                life.update(lives)
                
                if lives <=0:
                    mode = "end"
                    
            if points >=360:
                mode = "win"
        
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
        pygame.mixer.music.play(loops=-1)
    else:
        print("No Sound")
        
    pygame.mouse.set_visible(True)
        
    buttons = [Button("BACK", [500,950], 1)]
    
    bgImage=pygame.image.load("Art/Background/dead_Screen.png")
    bgRect = bgImage.get_rect()
    while mode=="end":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                     mode="start"
                     
            elif event.type == pygame.MOUSEMOTION:
               for button in buttons:
                   button.collidePoint(event.pos, clicked) 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                    for button in buttons:
                        button.collidePoint(event.pos, clicked)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = False
                    for button in buttons:
                        if button.collidePoint(event.pos, clicked):
                            if button.name == "BACK":
                                mode="start"
            
        screen.blit(bgImage, bgRect)
        
        for button in buttons:
            screen.blit(button.image, button.rect)
        
        
        pygame.display.flip()
        clock.tick(60)
        
        
    #-----------------------Win screen----------------------------------#
    if sound:
        pygame.mixer.music.load("Music/Background/You_Win!.mp3")
        pygame.mixer.music.set_volume(.25)
        pygame.mixer.music.play(loops=-1)
    else:
        print("No Sound")
        
    pygame.mouse.set_visible(True)
        
    buttons = [Button("BACK", [500,950], 1)]
    
    bgImage=pygame.image.load("Art/Background/WIN.png")
    bgRect = bgImage.get_rect()
    while mode=="win":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                     mode="start"
                     
            elif event.type == pygame.MOUSEMOTION:
               for button in buttons:
                   button.collidePoint(event.pos, clicked) 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
                    for button in buttons:
                        button.collidePoint(event.pos, clicked)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicked = False
                    for button in buttons:
                        if button.collidePoint(event.pos, clicked):
                            if button.name == "BACK":
                                mode="start"
            
        screen.blit(bgImage, bgRect)
        
        for button in buttons:
            screen.blit(button.image, button.rect)
        
        
        pygame.display.flip()
        clock.tick(60)
        
