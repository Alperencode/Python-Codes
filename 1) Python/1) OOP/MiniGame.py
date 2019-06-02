#%%
class Player:
    def __init__(self,hp,damage):
        self.hp = hp
        self.damage = damage
    
    def attack(self,enemy):
        enemy.hp -= self.damage

class Enemy:
    def __init__(self,hp,damage):
        self.hp = hp
        self.damage = damage

    def attack(self,player):
        player.hp -= self.damage

player = Player(500,50)

enemys = []

for i in range(10):
    enemys.append(Enemy(100,50))
























#%%