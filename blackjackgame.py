import blackjack 
import random
from time import sleep

players_hand = list()
opponents_hand = list()
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
suits = ["Michael Whalen", "Gabriel Liberov", "Izzy Zoltan", "Andrew Rosini"]

def player_cards():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    suits = ["Michael Whalen", "Gabriel Liberov", "Izzy Zoltan", "Andrew Rosini"]
    
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
        random_suit = random.choice(suits)
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
player_cards()

sleep(2.5)

def opponents_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    suits = ["Michael Whalen", "Gabriel Liberov", "Izzy Zoltan", "Andrew Rosini"]
    
    face_up_value = random.choice(cards)
    if face_up_value == 10:
        possible_cards = ["10", "Jack", "Queen", "King"]
        random_card = random.choice(possible_cards)
        suits = ["Michael Whalen", "Gabriel Liberov", "Izzy Zoltan", "Andrew Rosini"]
        random_suit = random.choice(suits)
        face_up_card = (f"Your opponent's deck consists of a faceup card, which is the {random_card} of {random_suit}")
    elif face_up_value < 10:
        suits = ["Michael Whalen", "Gabriel Liberov", "Izzy Zoltan", "Andrew Rosini"]
        random_suit = random.choice(suits)
        face_up_card = (f"Your opponent's deck consists of a faceup card, which is the {face_up_value} of {random_suit}")
    elif face_up_value == 11:
        random_suit = random.choice(suits)
        cards.remove(11)
        face_up_card = (f"Your opponent's deck consists of a faceup card, which is the ace of {random_suit}")
    opponents_hand.append(face_up_value)

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
    opponents_hand.append(face_down_value)

    print(f"{face_up_card}, and one facedown card.")
opponents_card()

sleep(2.5)

hit_or_stand = input("Would you like to hit or stand? Hit/Stand: ")
if hit_or_stand == "Hit":
    new_card_value = random.choice(cards)
    if new_card_value == 10:
        possible_cards = ["10", "Jack", "Queen", "King"]
        random_card = random.choice(possible_cards)
        suits = ["Michael Whalen", "Gabriel Liberov", "Izzy Zoltan", "Andrew Rosini"]
        random_suit = random.choice(suits)
        new_card = (f"Your new card is the {random_card} of {random_suit}.")
    elif new_card_value < 10:
        suits = ["Michael Whalen", "Gabriel Liberov", "Izzy Zoltan", "Andrew Rosini"]
        random_suit = random.choice(suits)
        new_card = (f"Your new card is the {new_card_value} of {random_suit}.")
    elif new_card_value == 11:
        random_suit = random.choice(suits)
        new_card = (f"Your new card is the ace of {random_suit}.")
        if sum(players_hand) + 11 > 21:
            new_card_value = 1
        elif sum(players_hand) + 11 < 21:
            new_card_value = input("Would you like your ace to be valued as a 1 or 11? 1/11: ")
            if new_card_value == "1":
                new_card_value = 1
            elif new_card_value == "11":
                new_card_value = 11
    players_hand.append(new_card_value)
    players_sum = sum(players_hand)