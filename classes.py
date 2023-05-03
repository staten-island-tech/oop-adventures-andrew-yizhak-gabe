class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health 
class Player(Character):
    def __init__(self, name, health):
        super().__init__(self, name, health)
class NPC(Character):
    def __init__(self, name):
        super().__init__(self, name)
class Enemy(Character):
    def __init__(self, name, health):
        super().__init__(self, name, health)
class Boss(Enemy):
    def __init__(self, name, health):
        super().__init__(self, name, health)