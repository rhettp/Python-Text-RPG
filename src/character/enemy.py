
##### Enemy Setup #####

# Base enemy class
class Enemy:
    def __init__(self, name, max_hp, max_hit, gold, xp):
        self.name = name
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.max_hit = max_hit
        self.gold = gold
        self.xp = xp

    def is_dead(self):
        return self.hp <= 0

    def display_stats(self):
        print("Enemy: {}    HP: {}/{}\n".format(self.name, self.hp, self.max_hp))

# Goblin enemy
class Goblin(Enemy):
    def __init__(self):
        super().__init__(name = "Goblin", max_hp = 25, max_hit = 5, gold = 25, xp = 15)

# Slime enemy
class Slime(Enemy):
    def __init__(self):
        super().__init__(name = "Slime", max_hp = 20, max_hit = 4, gold = 20, xp = 10)

# Giant Spider enemy
class Giant_Spider(Enemy):
    def __init__(self):
        super().__init__(name = "Giant Spider", max_hp = 35, max_hit = 8, gold = 40, xp = 30)

# Ghoul enemy    
class Ghoul(Enemy):
    def __init__(self):
        super().__init__(name = "Ghoul", max_hp = 40, max_hit = 10, gold = 50, xp = 35)

# Ogre enemy
class Ogre(Enemy):
    def __init__(self):
        super().__init__(name = "Ogre", max_hp = 60, max_hit = 15, gold = 100, xp = 80)

# Crocolisk
class Crocolisk(Enemy):
    def __init__(self):
        super().__init__(name = "Crocolisk", max_hp = 50, max_hit = 12, gold = 80, xp = 70)

# Skeleton enemy
class Skeleton(Enemy):
    def __init__(self):
        super().__init__(name = "Skeleton", max_hp = 75, max_hit = 22, gold = 150, xp = 170)

# Zombie enemy
class Zombie(Enemy):
    def __init__(self):
        super().__init__(name = "Zombie", max_hp = 65, max_hit = 18, gold = 135, xp = 150)

# Black Dragon
class Black_Dragon(Enemy):
    def __init__(self):
        super().__init__(name = "Black Dragon", max_hp = 150, max_hit = 30, gold = 500, xp = 500)

forest_enemies = [Goblin(), Slime()]
mine_enemies = [Giant_Spider(), Ghoul()]
swamp_enemies = [Ogre(), Crocolisk()]
graveyard_enemies = [Skeleton(), Zombie()]
lair_enemies = [Black_Dragon()]