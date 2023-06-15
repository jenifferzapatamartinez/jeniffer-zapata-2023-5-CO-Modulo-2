import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY


class Ballet(Sprite):
    BULLET_SIZE=pygame.transform.scale(BULLET,(10,20))
    BULLET_SIZE_ENEMY=pygame.transform.scale(BULLET_ENEMY,(9,32))
    BULLETS={'player':BULLET_SIZE,'enemy':BULLET_SIZE_ENEMY}
    
    def __init__(self, spaceship):
        self.image=self.BULLETS[spaceship.type]