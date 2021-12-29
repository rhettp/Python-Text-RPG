
##### Enemy Setup #####

# Base enemy class
class Enemy:
    def __init__(self, name, max_hp, damage, gold):
        self.name = name
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.damage = damage
        self.gold = gold

    def is_dead(self):
        return self.hp <= 0

    def display_stats(self):
        print("Enemy: {}    HP: {}/{}\n".format(self.name, self.hp, self.max_hp))

# Goblin enemy subclass
class Goblin(Enemy):
    def __init__(self):
        super().__init__(name = "Goblin", max_hp = 25, damage = 2, gold = 25)