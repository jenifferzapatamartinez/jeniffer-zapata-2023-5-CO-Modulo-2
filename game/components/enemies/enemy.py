import pygame
import random

from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_1,ENEMY_2,ENEMY_3, SCREEN_HEIGHT, SCREEN_WIDTH

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
        self.image = pygame.transform.scale(self.LEVENEMY, (self.ENEMY_WHIDTH,self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0 , 20)]
        self.rect.y = self.Y_POS
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 100)
        self.index = 0
        self.type='enemy'
        self.shooting_time=random.randint(30, 50)
       
    def level_game(self):
        ship=0
        size=0
        time=0
        if self.level==1:
            ship=ENEMY_1
            size=random.randint(0, 5)
            time=random.randint(3, 4)
        elif self.level==2:
            ship=ENEMY_2
            size=random.randint(5, 10)
            time=random.randint(4, 5)
        elif self.level==3:
            ship=ENEMY_3
            size=random.randint(10, 15)
            time=random.randint(5, 6) 
        
        self.enemy_ship(ship,size,time)
        
    def enemy_ship(self,ship,size,time):
        self.speed_x = self.SPEED_X+time
        self.speed_y = self.SPEED_Y+time-1
        self.image = pygame.transform.scale(ship, (self.ENEMY_WHIDTH+size,self.ENEMY_HEIGHT+size))

    def update(self, ships, game):
        level = game.level_game

        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)

        if level != None and level < 4:
            self.level = level
            self.level_game()
        
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

    def draw(self, screen):       
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.index = 0

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet=Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)