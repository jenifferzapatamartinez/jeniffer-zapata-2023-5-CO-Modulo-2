from game.components.enemies.enemy import Enemy


class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.level_game=1
    def update(self,level):
        self.add_enemy()
        for enemy in self.enemies:
            return enemy.update(self.enemies,level)
        

    def draw(self, screen):
        for enemy in self.enemies: 
            enemy.draw(screen)            

    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy = Enemy()
            self.enemies.append(enemy)
        #Para dos enemigos
        #elif len(self.enemies) == 1:
         #   enemy2 = Enemy(self.index)
         #   enemy2.multy_enemy(2)
         #   self.enemies.append(enemy2)

  