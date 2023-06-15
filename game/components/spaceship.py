import pygame
from pygame.sprite import Sprite
import random

from game.components.bullets.bullet import Bullet
from game.utils.constants import SPACESHIP, SCREEN_WIDTH ,SCREEN_HEIGHT


class Spaceship(Sprite):
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60 
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    X_POS = (SCREEN_WIDTH // 2) - SPACESHIP_WIDTH
    Y_POS = 500

    def __init__(self):
        self.image=pygame.transform.scale(SPACESHIP,(self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type='player'
        self.shooting_time=random.randint(30, 50)
       

    def update(self, game, user_input):
        if user_input[pygame.K_SPACE]:#Al precionar espacio dispara la nave
            self.shoot(game.bullet_manager)
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
           self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -=10
        else:
            self.rect.x = SCREEN_WIDTH - self.SPACESHIP_WIDTH
    
    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x +=10
        else:
            self.rect.x =0

    def move_up(self):
        if self.rect.y > self.HALF_SCREEN_HEIGHT:
            self.rect.y -=10
    
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - self.SPACESHIP_HEIGHT:
            self.rect.y +=10

    def draw(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, bullet_manager):#Disparar desde la nave
        #current_time = pygame.time.get_ticks()
        #if self.shooting_time <= current_time:
            bullet=Bullet(self)
            bullet_manager.add_bullet(bullet)
            #self.shooting_time += random.randint(30, 50)