import pygame, sys, math, random
from Hud import *
from Pellet import *
from Head import *

pygame.init()

if not pygame.font: print("Warning, fonts disabled")

size = [1000,900]
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock();

score = Hud ("Score: ",[0,0])


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




    screen.fill([30,40,50])
    screen.blit(score.image, score.rect)
    pygame.display.flip()
    clock.tick(60)
    # print(clock.get_fps())
