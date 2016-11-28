# Pacman at it's finest
import random
import pygame
import sys
import time

from pygame.locals import*
pygame.init()
FPSCLOCK - pygmae.time.Clock()

FPS = 15
WINDOWWIDTH = 475
WINDOWHEIGHT = 625
CELLSIZE = 25
BLACK = (0,0,0)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
STOP = 'stop'

# Variables
x = 0
y = 0

Px = 225
Py = 475
G1x = 225
G1y = 225
G2x = 225
G2y = 100
G3x = 225
G3y = 350
G4x = 225
G4y = 575
G5x = 425
G5y = 300
G6x = 25
G6y = 300
G7x = 425
G7y = 25
G8x = 25
G8y = 25

C = 0
Collision = 0 #(lika hægt að gera false)
Coin = 0

Level = 1

Pdirect = STOP
G1direct = LEFT
G2direct = RIGHT
G3direct = LEFT
G4direct = RIGHT

#Images

# Setting up the Game
Game = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,1,0,
0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,0,1,0,1,1,1,0,1,1,1,0,1,0,0,0,0,
0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,1,0,1,0,0,0,0,
0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,
0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,
0,1,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0,32)
DISPLAYSURF.fill(BLACK)
for i in range(475):
    if(Game[i] == 0):
        DISPLAYSURF.blit(brick,(x,y))
    if(Game[i] == 1):
        DISPLAYSURF.blit(coin,(x,y))
    if(Game[i] == 2):
        DISPLAYSURF.blit(blank,(x,y))
    x += 25
    if(((i + 1) % 19) == 0):
        y += 25
        x = 0

x = 0
y = 0

DISPLAYSURF.blit(Level1, (150,225))
pygame.display.update()
time.sleep(5)

while True:

#Background
    for i in range(475):
    if (Game[i] == 0):
        DISPLAYSURF.blit(brick, (x, y))
    if (Game[i] == 1):
        DISPLAYSURF.blit(coin, (x, y))
    if (Game[i] == 2):
        DISPLAYSURF.blit(blank, (x, y))
    x += 25
    if (((i + 1) % 19) == 0):
        y += 25
        x = 0

x = 0
y = 0

DISPLAYSURF.blit(title,(200,275))





# Level Completion
Coln - 0
for i in range(475):
    if(Game[i] == 1):
        Coin += 1
    if(Coin -- 160):
        Level +-1

if((Level == 2) and (Coin == 160)):
    DISPLAYSURF.blit(Level2, (150,225))
if((Level -- 3) and (Coin -- 160)):
    DISPLAYSURF.blit(Level3, (150,225))
if(Level == 4):
    DISPLAYSURF.blit(YW, (150,225))

# Restarts the Game
if(((Level == 3) and (Coin == 160)) or ((Level == 2) and (Coin == 160)) or (Collision == 1) or (Level == 4)):
    pygame.display.update()
    if(Collision -- 1):
        time.slpeep(3)
    if((Collision == 1) and (Level == 1)):
        DISPLAYSURF.blit(Level1, (150,225))
    if((Collision == 1) and (Level == 2)):
        DISPLAYSURF.blit(Level2, (150,225))
    if((Collision -- 1) and (Level -- 3)):