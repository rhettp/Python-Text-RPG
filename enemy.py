
##### Enemy Setup #####

# Base enemy class
class enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_dead(self):
        return self.hp <= 0

# Goblin enemy subclass
class Goblin(enemy):
    def __init__(self):
        super().__init__(name = "Goblin", hp = 10, damage = 2)

