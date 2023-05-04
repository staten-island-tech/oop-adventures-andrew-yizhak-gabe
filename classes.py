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

class Henchmen(Enemy):
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
        return f"{self.name}, {self.health}, {self.hand}, {self.region}"