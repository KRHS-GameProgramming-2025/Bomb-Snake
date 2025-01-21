import pygame, sys, math, random
from Hud import *
from Pellet import *
from Head import *
from Bomb import *
from Tail import *
from Wall import *

pygame.init()
if not pygame.font: print("Warning, fonts disabled")

size = [1000,900]
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock();

score = Hud ("Score: ",[0,0])
player = Head(4,[1000/5, 900/2])
snake = [player]
snake += [Tail(4,[1000/5, 900/2])]

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
        elif event.type == pygame.KEYUP:
            if event.key == pygame. K_a or event.key == pygame.K_LEFT:
                player.goKey("sleft")
            elif event.key == pygame. K_d or event.key == pygame.K_RIGHT:
                player.goKey("sright")
            elif event.key == pygame. K_w or event.key == pygame.K_UP:
                player.goKey("sup")
            elif event.key == pygame. K_s or event.key == pygame.K_DOWN:
                player.goKey("sdown")
                
                
                
    for hittingPellet in pellets:
        for hitPellet in pellets:
          if hittingPellet.pelletCollide(hitPellet):
              if hittingPellet.kind == "player":
                  pellets.remove(hitPellets)
                  kills += 1
    player.update(size)
    

    screen.fill([30,40,50])
    for pellet in pellets:
        screen.blit(pellet.image, pellet.rect)
    screen.blit(score.image, score.rect)
    screen.blit(player.image, player.rect)
    screen.blit(tail.image, tail.rect)
    pygame.display.flip()
    clock.tick(60)
    # print(clock.get_fps())
