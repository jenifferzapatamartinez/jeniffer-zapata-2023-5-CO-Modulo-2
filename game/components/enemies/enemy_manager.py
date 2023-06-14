from game.components.enemies.enemy import Enemy


class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.index=0

    def update(self):
        self.add_enemy()
        
        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies: 
            enemy.draw(screen)            

    def add_enemy(self):
        self.index +=1
        if len(self.enemies) < 1:
            enemy = Enemy()
            enemy.multy_enemy(self.index)
            if self.index == 2:
                self.index=0
            self.enemies.append(enemy)
        #Para dos enemigos
        #elif len(self.enemies) == 1:
         #   enemy2 = Enemy(self.index)
         #   enemy2.multy_enemy(2)
         #   self.enemies.append(enemy2)

  