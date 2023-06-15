import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1,ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH



class Enemy(Sprite):
    ENEMY_WHIDTH = 40
    ENEMY_HEIGHT = 60
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500,
                  550,600,650,700,750,800,850,900,950,1000,1050]
    Y_POS= 10
    SPEED_X = 5 
    SPEED_Y = 4
    MOV_X = { 0: 'left', 1: 'right' }
    LEVENEMY=ENEMY_1
    LEVEL=1

    def __init__(self):
        self.level=self.LEVEL
        self.i=0
        self.i2=0
        self.enemy = self.LEVENEMY #self.level_game_enemy()
        self.image = pygame.transform.scale(self.enemy, (self.ENEMY_WHIDTH,self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0 , 20)]
        self.rect.y = self.Y_POS
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 100)
        self.index = 0
       
       
    def level_game_enemy(self):
        if self.level==1:
            return ENEMY_1
        elif self.level==2:
            return ENEMY_2
    
    def level_game(self):
        print(f"en lelvel {self.level}")
        if self.level==1:
            self.speed_x = self.SPEED_X+5
            self.speed_y = self.SPEED_Y+5
            self.enemy=ENEMY_1
            self.image = pygame.transform.scale(self.enemy, (self.ENEMY_WHIDTH,self.ENEMY_HEIGHT))
        
        elif self.level==2:
            self.speed_x = self.SPEED_X+10
            self.speed_y = self.SPEED_Y+10
            self.enemy=ENEMY_2
            self.image = pygame.transform.scale(self.enemy, (self.ENEMY_WHIDTH,self.ENEMY_HEIGHT))
        
            

    def update(self, ships,level):
        
       
        if level!=None and level<3 :
            self.level=level
            self.level_game()

        self.rect.y += self.speed_y
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movement_x()

        else:
            self.rect.x += self.speed_x
            self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
            self.level +=1
            return self.level
            #self.i +=1
            #print(f"contaor: {LEVEL}")


    def draw(self, screen):       
        #self.i +=1
        #print(f"contaor: {self.i}")
        if self.i==1:
            self.level +=1
            #self.level_game()
            #print(f"contar level: {self.level}")
            '''
            if self.i2==1:
                self.level=1
                self.level_game()
            elif self.i2==2:
                self.level=2
                self.level_game()'''

        screen.blit(self.image, (self.rect.x, self.rect.y))
        
      
            
    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right' or (self.rect.x >= SCREEN_WIDTH)):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left' or (self.rect.x <= 10)):
            self.movement_x = 'right'
            self.index = 0

    def multy_enemy(self,enemy):     
            self.i =enemy
            self.level_game_enemy()
            self.level_game()
     