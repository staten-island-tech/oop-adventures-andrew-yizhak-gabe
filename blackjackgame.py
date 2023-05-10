import blackjack 
import random

players_hand = list()
opponents_hand = list()

random_suit = print(random.choice(blackjack.deck_suits))
random_value = print(random.choice(blackjack.deck_values))

if random_value == 10:
    deck_faces = ["Ten", "Jack", "Queen", "King"]
    random_face = random.choice(deck_faces)
    print(f"{random_face} of {random_suit}")