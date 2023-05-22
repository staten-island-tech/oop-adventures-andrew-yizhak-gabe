import uuid
import random
birds = ['Albatross','Auklet','Bittern','Blackbird','Bluebird','Bunting','Chickadee','Cormorant','Cowbird','Crow','Dove','Dowitcher','Duck','Eagle','Egret','Falcon','Finch','Flycatcher','Gallinule','Gnatcatcher','Godwit','Goldeneye','Goldfinch','Goose','Grackle','Grebe','Grosbeak','Gull','Hawk','Heron','Hummingbird','Ibis','Jaeger','Jay','Junco','Kingbird','Kinglet','Kite','Longspur','Loon','Magpie','Meadowlark','Merganser','Murrelet','Nuthatch','Oriole','Owl','Pelican','Petrel','Pewee','Phalarope','Phoebe','Pigeon','Pipit','Plover','Pterodactyl','Puffin','Quail','Rail','Raven','Redstart','Sandpiper','Sapsucker','Scaup','Scoter','Shearwater','Shrike','Skua','Sparrow','Storm-Petrel','Swallow','Swift','Tanager','Teal','Tern','Thrasher','Thrush','Titmouse','Towhee','Turnstone','Vireo','Vulture','Warbler','Wigeon','Woodpecker','Wren','Yellowlegs','Zinglebird']
regions = ['Potassium Palace', 'Ripe Ravine', 'Plantain Plateau', 'Fruity Field']

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
        return f"{self.name}, {self.health}, {self.hand}, {self.region}"

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

random_bird = random.choice(birds)
random_region = random.choice(regions)

henchman = Henchman(random_bird, 30, "HAND")
enforcer = Enforcer(random_bird, 50, "HAND")
Lil_Nas_X = Boss("Lil_Nas_X", 50, "HAND", "Fruity Fields")
Tweety = Boss("Tweety", 100, "HAND", 'Fruity Field') #Player Health After: 150#
Steve = Boss("S.T.E.V.E", 200, "HAND", 'Ripe Ravine') #Player Health After: 250#
Terrence = Boss("Terrence", 400, "HAND", 'Plantain Plateau') #Player Health After: 450#
Private = Boss("Private", 700, "HAND", "NewNana") #Player Health After: 800#
Rico = Boss("Rico", 1100, "HAND", "NewNana") #Player Health After: 1350#
Kowalski = Boss("Kowalski", 1800, "HAND", "NewNana") #Player Health After: 2250#
Skipper = Boss("Skipper", 3000, "HAND", "NewNana") #Player Health After: 3750#
King_Ghidorah = Boss("King Ghidorah", 5000, "HAND", 'Potassium Palace') #Player Health After: 6500#
Biggest_Bird = Boss("Biggest Bird", 10000, "HAND", "Big Bird's Bar")