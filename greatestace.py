"""
Left to do:
    - Code consistent blackjack function that can be used for each level.
    - Add in information, through classes, regarding characters.
    - Create information regarding setting, text, and other, finer details about the game.
    - Enter a heart system that allows the player to lose or gain hearts based on what the NPC will gamble.
Note: Gabe and Izzy, add to this if you think of anything else to do.
"""

"""Classes for Characters -- added User, Tom, and Jiminie -- going to add Ace, and then the Mafia Bosses"""
import uuid
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    new_id = str(uuid.uuid4())

class Tom(User):
    def __init__(self, id, name, introductory_game):
        super().__init__(id, name)
        self.introductory_game = introductory_game
    def __str__(self):
        return f"{self.id}, {self.name}, {self.introductory_game}."

class Jiminie(User):
    def __init__(self, id, name, duplication):
        super().__init__(id, name)
        self.duplication = duplication
    def __str__(self):
        return f"{self.id}, {self.name}, {self.duplication}"