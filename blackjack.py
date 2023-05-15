def blackjack():
    import random
    from time import sleep
    
    players_hand = list()
    opponents_hand = list()
    global card
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    global suits
    suits = ["Michael Whalen", "Gabriel Liberov", "Izzy Zoltan", "Andrew Rosini"]

    def player_cards():
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
    while hit_or_stand == "Hit":
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
        print(new_card)
        if players_sum > 21:
            print("Bust! Your opponent automatically wins!")
            player_position = "Bust"
            break
        hit_or_stand = input("Would you like to hit or stand? Hit/Stand: ")
    if hit_or_stand == "Stand":
        players_sum = sum(players_hand)
        player_position = players_sum
        print(f"Your total card value is {players_sum}. If your opponent has a higher card value than {players_sum}, you will lose. If they have a lower card value than {players_sum}, you will win.")
    
    while player_position == players_sum:
        opponents_sum = sum(opponents_hand)
        if opponents_sum > players_sum:
            print(f"Your opponents has gained a higher score than you, {opponents_sum}. You will now lose the number of hearts you gambled at the beginning of the round.")
            break
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
        opponents_hand.append(new_card_value)
        opponents_sum = sum(opponents_hand)
        if opponents_sum > 21:
            print("Your opponent has busted. You have defeated your oppenent, and absorbed half of their hearts.")
            break
        elif opponents_sum < 21 and opponents_sum < players_sum:
            hit_or_stand = player_position
        elif opponents_sum < 21 and opponents_sum > players_sum:
            print(f"Your opponents has gained a higher score than you, with a total of {opponents_sum}. You will now lose the number of hearts you gambled at the beginning of the round.")
            break
    while player_position == "Bust":
        print("Your opponent has won. You will now lose the number of hearts you gambled at the beginning of the round.")
        break
blackjack()