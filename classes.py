import uuid
class User:
    def __init__(self, name):
        self.name = name
    new_id = str(uuid.uuid4())

class Enemy(User):
    def __init__(self, name, health):
        super().__init__(name)
        self.health = health
    def __str__(self):
        return f"{self.name}, {self.health}"

class Henchman(Enemy):
    def __init__(self, name, health, hand):
        super().__init__(name, health)
        self.hand = hand
    def __str__(self):
        return f"{self.name}, {self.health}, {self.hand}"

class Enforcer(Enemy):
    def __init__(self, name, health, hand):
        super().__init__(name, health)
        self.hand = hand
    def __str__(self):
        return f"{self.name}, {self.health}, {self.hand}"

class Boss(Enforcer):
    def __init__(self, name, health, hand, region):
        super().__init__(name, health, hand)
        self.region = region
    def __str__(self):
        return f"{self.name}, {self.health}, {self.hand}"

enemies = []
henchmen = []
enforcers = []
bosses = []

def create_new_enemy(name, health):
    new_enemy = Enemy(name, health)
    enemies.append(new_enemy)
    for enemy in enemies:
        print(enemy)

def create_new_henchman(name, health, hand):
    new_henchman = Henchman(name, health, hand)
    henchmen.append(new_henchman)
    for henchman in henchmen:
        print(henchman)

def create_new_enforcer(name, health, hand):
    new_enforcer = Enforcer(name, health, hand)
    enforcers.append(new_enforcer)
    for enforcer in enforcers:
        print(enforcer)

def create_new_boss(name, health, hand, region):
    new_boss = Boss(name, health, hand, region)
    bosses.append(new_boss)
    for boss in bosses:
        print(boss)