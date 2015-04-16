import sys
from random import randint, choice
from math import sin, cos, radians
import os

#os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,80)

import pygame
from pygame.sprite import Sprite
from pygame.locals import *


playerPic = pygame.image.load('falcon.png')
player_rect = playerPic.get_rect()



credits = pygame.image.load("bountyLoot.png")
credit_rect = credits.get_rect()
credit_count = 0


pygame.init()
screen = pygame.display.set_mode((1500, 1000), 0, 32)
clock = pygame.time.Clock()
pygame.display.set_caption('Beggars Payback')

font = pygame.font.SysFont("monospace",30)

def checkCollision(rect1,rect2):
    return rect1.colliderect(rect2)

def winner():
    screen_w, screen_h = 1500, 1000
    background = 0, 0, 0

    screen = pygame.display.set_mode(
                (screen_w, screen_h), 0, 32)

    font = pygame.font.SysFont("monospace",60)
    font2 = pygame.font.SysFont("monospace",40)
    
    
    while True:
        time_passed = clock.tick(50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

        if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
            exit_game()

        
        label = font.render("You Won!! You paid Jabba in Full.",1,(255,255,0))
        label_pos = label.get_rect(centerx=screen.get_width()/2,centery = screen.get_width()/2)
        label2 = font2.render("Try not to be a scruffy nerf herder from here on out...",1,(255,255,0))
        label2_pos = label.get_rect(centerx = screen.get_width()/2,centery = screen.get_width()/2 + 70) 

        screen.fill(background)
        screen.blit(label,label_pos)
        screen.blit(label2,label2_pos)
        screen.blit(playerPic, (screen.get_width()/2, screen.get_height()/2 - 50))
        

        pygame.display.flip()

def welcome():
    screen_w, screen_h = 1500, 1000
    background = 0, 0, 0

    screen = pygame.display.set_mode((screen_w, screen_h), 0, 32)

    font = pygame.font.SysFont("monospace",30)
    
    
    while True:
        time_passed = clock.tick(50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

        if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
            exit_game()

        
        label = font.render("You have a debt on your head. Pick up the coins to pay Jabba the Hutt back.",1,(255,255,0))
        label_pos = label.get_rect(centerx=screen.get_width()/2,centery = screen.get_width()/2)
        label2 = font.render("Each level you need to pick up 15 coins to move onto the next level." ,1, (255,255,0))
        label2_pos = label2.get_rect(centerx=screen.get_width()/2,centery = screen.get_width()/2 + 35)
        label25 = font.render("Use the arrow keys to fly your ship around",1,(255,255,0))
        label25_pos = label25.get_rect(centerx=screen.get_width()/2,centery = screen.get_width()/2 + 70)
        label3 = font.render("Press enter to start the game." ,1, (255,255,0))
        label3_pos = label3.get_rect(centerx=screen.get_width()/2,centery = screen.get_width()/2 + 110)

        if(pygame.key.get_pressed()[pygame.K_RETURN]):
            levelOne()

        screen.fill(background)
        screen.blit(label,label_pos)
        screen.blit(label2,label2_pos)
        screen.blit(label25,label25_pos)
        screen.blit(label3,label3_pos)
        screen.blit(playerPic, (screen.get_width()/2, screen.get_height()/2 - 50))
        

        pygame.display.flip()

def runGame(badGuy, num_of_baddies,level):
    screen_w, screen_h = 1500, 1000
    background = 0, 0, 0
    credit_count = 0
   
    enemyPic = badGuy
    enemy_rect = enemyPic

    global playerPic

    if(num_of_baddies == 1):
        enemyStartX = randint(0,screen_w -80)
        enemyStartY = randint(0,screen_h -50)
        enemy_rect.x = enemyStartX
        enemy_rect.y = enemyStartY
        
    
    elif(num_of_baddies == 2):
        enemy2 = enemyPic
        enemy2_rect = enemy2.get_rect()

        enemyStartX = randint(0,screen_w -80)
        enemyStartY = randint(0,screen_h -50)
    
        enemy_rect.x = enemyStartX
        enemy_rect.y = enemyStartY

        enemy2X = randint(0,screen_w -80)
        enemy2Y = randint(0,screen_h -50)
        enemy2_rect.x = enemy2X
        enemy2_rect.y = enemy2Y
    
    elif(num_of_baddies == 3):
        enemy2 = enemyPic
        enemy2_rect = enemy2.get_rect()
        enemy3 = enemyPic
        enemy3_rect = enemy3.get_rect()

        enemyStartX = randint(0,screen_w -80)
        enemyStartY = randint(0,screen_h -50)
    
        enemy_rect.x = enemyStartX
        enemy_rect.y = enemyStartY

        enemy2X = randint(0,screen_w -80)
        enemy2Y = randint(0,screen_h -50)
        enemy2_rect.x = enemy2X
        enemy2_rect.y = enemy2Y

        enemy3X = randint(0,screen_w -80)
        enemy3Y = randint(0,screen_h -50)
        enemy3_rect.x = enemy3X
        enemy3_rect.y = enemy3Y 


    #start position for the player
    playerStartX = 260
    playerStartY = 300
    
    player_rect.x=playerStartX
    player_rect.y=playerStartY

    creditX = randint(0, screen_w -50)
    creditY = randint(0, screen_h-80)
    credit_rect.x = creditX
    credit_rect.y = creditY
    
    while True:
        time_passed = clock.tick(50)
        label = font.render("Level " + str(level) + ": Credits: "+ str(credit_count),1,(255,255,0))
        label_pos = label.get_rect(centerx=screen.get_width()/2)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

        if credit_count == 15:
            return
        
        if(num_of_baddies == 1):   
            enemyStartX +=12
            enemy_rect.x +=12
            if(enemyStartX >= screen.get_width()):
                enemyStartX = 0 - enemyStartX
                enemy_rect.x = enemyStartX
                enemyStartY = randint(0,screen_w-80)
                enemy_rect.y = enemyStartY

            if checkCollision(enemy_rect,player_rect):
                credit_count = 0
                screen.blit(label,(label_pos))

            if checkCollision(enemy_rect,credit_rect):
                credit_count -= 1
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(label,(label_pos))
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)

        elif(num_of_baddies == 2):
            enemyStartX +=12
            enemy_rect.x +=12
            if(enemyStartX >= screen.get_width()):
                enemyStartX = 0 - enemyStartX
                enemy_rect.x = enemyStartX
                enemyStartY = randint(0,screen_w-80)
                enemy_rect.y = enemyStartY

            enemy2X +=12
            enemy2_rect.x +=12
            if(enemy2X >= screen.get_width()):
                enemy2X = 0 - enemy2X
                enemy2_rect.x = enemy2X
                enemy2Y = randint(0,screen_w-80)
                enemy2_rect.y = enemy2Y

            if checkCollision(enemy_rect,player_rect):
                credit_count = 0
                screen.blit(label,(label_pos))

            if checkCollision(enemy_rect,credit_rect):
                credit_count -= 1
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(label,(label_pos))
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)

            if checkCollision(enemy2_rect,player_rect):
                credit_count = 0
                screen.blit(label,(label_pos))
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)

            if checkCollision(enemy2_rect,credit_rect):
                credit_count -= 1
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(label,(label_pos))
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)

        elif(num_of_baddies == 3):
            enemyStartX +=12
            enemy_rect.x +=12
            if(enemyStartX >= screen.get_width()):
                enemyStartX = 0 - enemyStartX
                enemy_rect.x = enemyStartX
                enemyStartY = randint(0,screen_w-80)
                enemy_rect.y = enemyStartY
            
            enemy2X +=12
            enemy2_rect.x +=12
            if(enemy2X >= screen.get_width()):
                enemy2X = 0 - enemy2X
                enemy2_rect.x = enemy2X
                enemy2Y = randint(0,screen_w-80)
                enemy2_rect.y = enemy2Y

            if checkCollision(enemy_rect,player_rect):
                credit_count = 0
                screen.blit(label,(label_pos))

            if checkCollision(enemy_rect,credit_rect):
                credit_count -= 1
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(label,(label_pos))
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)

            if checkCollision(enemy2_rect,player_rect):
                credit_count = 0
                screen.blit(label,(label_pos))
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)

            if checkCollision(enemy2_rect,credit_rect):
                credit_count -= 1
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(label,(label_pos))
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)
            
            enemy3X +=9
            enemy3_rect.x +=9
            if(enemy3X >= screen.get_width()):
                enemy3X = 0 - enemy3X
                enemy3_rect.x = enemy3X
                enemy3Y = randint(0,screen_w-80)
                enemy3_rect.y = enemy3Y
            if checkCollision(enemy3_rect,player_rect):
                credit_count = 0
                screen.blit(label,(label_pos))
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)

            if checkCollision(enemy3_rect,credit_rect):
                credit_count -= 1
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(label,(label_pos))
                screen.blit(credits, (creditX,creditY),credit_rect)

        if(pygame.key.get_pressed()[pygame.K_UP] !=0):
            playerStartY -=12
            player_rect.y -=12
            #print player_rect.y
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)
            
        if(pygame.key.get_pressed()[pygame.K_DOWN] !=0):
            playerStartY +=12
            player_rect.y +=12
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)
            
        if(pygame.key.get_pressed()[pygame.K_LEFT] !=0):
            playerStartX -=12
            player_rect.x -=12
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)
            
        if(pygame.key.get_pressed()[pygame.K_RIGHT] !=0):
            playerStartX +=12
            player_rect.x +=12
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w-50)
                creditY = randint(0, screen_h-80)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)

        if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
            exit_game()


        if(num_of_baddies == 1):
            screen.blit(enemyPic,(enemyStartX,enemyStartY))
            screen.blit(enemyPic,enemy_rect)
        ''' if(num_of_baddies == 1):
            screen.blit(enemyPic,(enemyStartX,enemyStartY))
            screen.blit(enemyPic,enemy_rect)
        elif(num_of_baddies ==2):
            screen.blit(enemyPic,(enemyStartX,enemyStartY))
            screen.blit(enemyPic,enemy_rect)
            screen.blit(enemy2, (enemy2X,enemy2Y))
            screen.blit(enemy2,enemy2_rect)
        elif(num_of_baddies == 3):
            screen.blit(enemyPic,(enemyStartX,enemyStartY))
            screen.blit(enemyPic,enemy_rect)
            screen.blit(enemy2, (enemy2X,enemy2Y))
            screen.blit(enemy2,enemy2_rect)
            screen.blit(enemy3, (enemy3X,enemy3Y))
            screen.blit(enemy3,enemy3_rect)
        '''
        screen.fill(background)
        screen.blit(playerPic, (playerStartX,playerStartY))
        screen.blit(label,label_pos)
        screen.blit(playerPic, player_rect)

        screen.blit(credits, (creditX,creditY),credit_rect)
        screen.blit(credits,credit_rect)
        screen.blit(label,label_pos)
        

        pygame.display.flip()

def levelOne():
    runGame(pygame.image.load('worm.png'),1,1)
    
    levelTwo()

def levelTwo():
    runGame(pygame.image.load('tie.png'),3,2)

    levelThree()

def levelThree():
    runGame(pygame.image.load('sd.png'),2,3)

    winner()

   

def exit_game():
    sys.exit()

welcome()
