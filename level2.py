import sys
from random import randint, choice
from math import sin, cos, radians

import pygame
from pygame.sprite import Sprite
from pygame.locals import *

from vec2d import vec2d

def checkCollision(player,credit):
    return player.colliderect(credit)

    '''for a, b in [(player,credit), (credit,player)]:
        if(insideRect(a.left,a.top,b))or insideRect(a.left, a.bottom, b) or(insideRect(a.right, a.top, b)) or(insideRect(a.right, a.bottom, b)):
            return True
    return False

def insideRect(x,y,rect):
    if(x>rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False
'''
class Creep(Sprite):


    #def collision_detection(rect1,rect2):       
    
    def __init__(   
            self, screen, img_filename, init_position, 
            init_direction, speed):
        
        Sprite.__init__(self)
        
        self.screen = screen
        self.speed = speed
        
        self.base_image = pygame.image.load('tie.png')
        self.image  = self.base_image

        bounds = self.image.get_rect()
       
        self.pos = vec2d(init_position)

        self.direction = vec2d(init_direction).normalized()
            
    def update(self, time_passed):
        
        self._change_direction(time_passed)
        
        self.image = pygame.transform.rotate(self.base_image, self.direction.angle)
        
        displacement = vec2d(    
            self.direction.x * self.speed * time_passed,
            self.direction.y * self.speed * time_passed)
        self.pos += displacement
        
        self.image_w, self.image_h = self.image.get_size()
        bounds_rect = self.screen.get_rect().inflate(
                        -self.image_w, -self.image_h)
        
        if self.pos.x < bounds_rect.left:
            self.pos.x = bounds_rect.left
            self.direction.x *= -1
        elif self.pos.x > bounds_rect.right:
            self.pos.x = bounds_rect.right
            self.direction.x *= -1
        elif self.pos.y < bounds_rect.top:
            self.pos.y = bounds_rect.top
            self.direction.y *= -1
        elif self.pos.y > bounds_rect.bottom:
            self.pos.y = bounds_rect.bottom
            self.direction.y *= -1
    
    def blitme(self):
        
        draw_pos = self.image.get_rect().move(
            self.pos.x - self.image_w / 2, 
            self.pos.y - self.image_h /2)
        self.screen.blit(self.image, draw_pos)

    _counter = 0

    def _change_direction(self,time_passed):
        self._counter += time_passed
        if self._counter > randint (400, 500):
            #self.direction.rotate(45 * randint(-1,1))
            self._counter = 0
   
   
		
	
	
#----------------------- end of class ----------------------------------------------    
playerPic = pygame.image.load('falcon.png')
credits = pygame.image.load("bountyLoot.png")
player_rect = playerPic.get_rect()
credit_rect = credits.get_rect()

def run_game():
    screen_w, screen_h = 1000, 1000
    background = 0, 0, 0
    enemyPi = 'tie.png'
    
    pygame.display.set_caption("Beggars Payback")
    
    tieFightersNum = 3
    credit_count = 0

    pygame.init()
    screen = pygame.display.set_mode(
                (screen_w, screen_h), 0, 32)
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("monospace",15)

    #start position for the player
    playerStartX = 260
    playerStartY = 300

    player_rect.x=playerStartX
    player_rect.y=playerStartY

    creditX = randint(0, screen_w)
    creditY = randint(0, screen_h)
    credit_rect.x = creditX
    credit_rect.y = creditY

    # Create N_CREEPS random creeps.
    tie = []    
    for i in range(tieFightersNum):
        tie.append(Creep(screen,
                            enemyPi, 
                            (   randint(0, screen_w), 
                                randint(0, screen_h)), 
                            (   choice([-1, 1]), 
                                choice([-1,1])),
                            0.2))
        
    while True:
        time_passed = clock.tick(80)
        label = font.render("Loot: "+ str(credit_count),1,(255,255,0))
        label_pos = label.get_rect(centerx=screen.get_width()/2)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

        if(pygame.key.get_pressed()[pygame.K_UP] !=0):
            playerStartY -=5
            player_rect.y -=5
            #print player_rect.y
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w)
                creditY = randint(0, screen_h)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)
                
        if(pygame.key.get_pressed()[pygame.K_DOWN] !=0):
            playerStartY +=5
            player_rect.y +=5
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w)
                creditY = randint(0, screen_h)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)
            
            
        if(pygame.key.get_pressed()[pygame.K_LEFT] !=0):
            playerStartX -=5
            player_rect.x -=5
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w)
                creditY = randint(0, screen_h)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)
            
            
        if(pygame.key.get_pressed()[pygame.K_RIGHT] !=0):
            playerStartX +=5
            player_rect.x +=5
            if checkCollision(credit_rect,player_rect):
                credit_count +=1
                screen.blit(label,(label_pos))
                creditX = randint(0, screen_w)
                creditY = randint(0, screen_h)
                credit_rect.x = creditX
                credit_rect.y = creditY
                screen.blit(credits, (creditX,creditY),credit_rect)
                screen.blit(credits,credit_rect)

        if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
            exit_game()

        
        screen.fill(background)
        screen.blit(playerPic, (playerStartX,playerStartY))
        screen.blit(playerPic, player_rect)
        screen.blit(credits, (creditX,creditY),credit_rect)
        screen.blit(credits,credit_rect)
        screen.blit(label,label_pos)
        
        # Update the enemies
        for enemy in tie:
            enemy.update(time_passed)
            enemy.blitme()

            '''if pygame.sprite.collide_rect(player1, enemy.Rect):
                collision_count +=1
'''
        pygame.display.flip()


     
def exit_game():
    sys.exit()


run_game()

