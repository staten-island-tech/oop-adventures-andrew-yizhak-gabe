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

def opponents_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    
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
    if face_up_value == 11 and random_card == "Jack":
        print("Blackjack! Your opponent gets an automatic win!")
opponents_card()












def player_draw():
    i = 0.1
    while i != 0:
        hit_or_stand = input("Would you like to hit or stand? HIT/STAND: ")
        if hit_or_stand == "HIT":
            cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
            new_card = random.choice(cards)
            if new_card == 11:
                current_sum = sum(players_hand)
                if current_sum + 11 > 21:
                    new_card == 1
                    players_hand.append(new_card)
                else:
                    new_card = input("Do you want your ace to be valued at 1 or 11? 1/11: ")
            else:
                current_sum = sum(players_hand)
                new_sum = current_sum + new_card
                if new_sum > 21:
                    print("Bust! You lose!")
                    i = 0
                else:
                    print(new_sum)
        elif hit_or_stand == "STAND":
            card_sum = sum(players_hand)
            print(f"The total sum of your cards is {card_sum}.")
            i = 0
player_draw()