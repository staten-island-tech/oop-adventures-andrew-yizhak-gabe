import blackjack 
import random

players_hand = list()
opponents_hand = list()

def player_cards():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    
    face_up_value = random.choice(cards)
    if face_up_value == 10:
        possible_cards = ["10", "Jack", "Queen", "King"]
        random_card = random.choice(possible_cards)
        suits = ["Michael Whalen", "Gabriel Liberov", "Izzy Zoltan", "Andrew Rosini"]
        random_suit = random.choice(suits)
        face_up_card = (f"Your faceup card is the {random_card} of {random_suit}")
    elif face_up_value < 10:
        suits = ["Michael Whalen", "Gabriel Liberov", "Izzy Zoltan", "Andrew Rosini"]
        random_suit = random.choice(suits)
        face_up_card = (f"Your faceup card is the {face_up_value} of {random_suit}")
    elif face_up_value == 11:
        cards.remove(11)
        face_up_card = (f"Your faceup card is the ace of {random_suit}")
    players_hand.append(face_up_value)

    face_down_value = random.choice(cards)
    if face_down_value == 10:
        possible_cards = ["10", "Jack", "Queen", "King"]
        random_card = random.choice(possible_cards)
        suits = ["Michael Whalen", "Gabriel Liberov", "Izzy Zoltan", "Andrew Rosini"]
        random_suit = random.choice(suits)
        face_down_card = (f"your facedown card is the {random_card} of {random_suit}.")
    elif face_down_value != 10:
        suits = ["Michael Whalen", "Gabriel Liberov", "Izzy Zoltan", "Andrew Rosini"]
        random_suit = random.choice(suits)
        face_down_card = (f"your facedown card is the {face_down_value} of {random_suit}.")
    players_hand.append(face_down_value)

    print(f"{face_up_card}, and {face_down_card}")
    if face_up_value == 11 and random_card == "Jack":
        print("Blackjack! You get an automatic win!")
player_cards()