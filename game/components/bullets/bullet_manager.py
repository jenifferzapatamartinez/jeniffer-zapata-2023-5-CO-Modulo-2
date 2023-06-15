import pygame


class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.player_bullets=[]

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                #game.playing = False  #Apagar el juego
                #Game over
                #pygame.time.delay(1000) #Cerrar el juego
                #break #Salir del if
        for bullet in self.player_bullets:#Disparo del jugador
            bullet.update(self.player_bullets)
            if bullet.rect.colliderect(game.enemy.rect) and bullet.owner == 'player':
                self.player_bullets.remove(bullet)
                #contiene el suseo de impactar con balas el enemigo
            
    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
       
        for bullet in self.player_bullets:
            bullet.draw(screen)
       
        
    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets)<1:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player' and len(self.player_bullets)<1:#Disparo jugador
            self.player_bullets.append(bullet)
