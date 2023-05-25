from time import sleep
from classes import Lil_Nas_X
delay = 3
health = 100

def blackjack():
    import random
    from time import sleep

    players_hand = list()
    opponents_hand = list()
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    suits = ["Michael Whalen", "Gabriel Liberov", "Izzy Zoltan", "Andrew Rosini"]
    global players_sum
    global opponents_sum

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

    sleep(3)

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

    sleep(3)

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
            print("Your opponent has busted. You have defeated your opponent.")
            break
        elif opponents_sum < 21 and opponents_sum < players_sum:
            hit_or_stand = player_position
        elif opponents_sum < 21 and opponents_sum > players_sum:
            print(f"Your opponent has gained a higher score than you, with a total of {opponents_sum}. You will now lose the number of hearts you gambled at the beginning of the round.")
            break
    while player_position == "Bust":
        print("Your opponent has won. You will now lose the number of hearts you gambled at the beginning of the round.")
        break

print("Narrator: You stroll out of the bar, eventually making your way to the neighborhood of Fruity Fields. There, you run into your sidekick, Australian Henriques.")
sleep(delay)
print("Australian Henriques: Bloody Yanks! I don't know why you're back here in Bananaland, with your bounty and all, but you should go.")
sleep(delay)
print("King Kong: Never mind that, Australian Henriques. Walk with me, there's someone I want you to meet.")
sleep(delay)
print("Narrator: The pair stroll on, passing signs of the dreadful Bird Mafia, the ones who put the bounty on you, all the way.")
sleep(delay)
print("Narrator: Together, you and Australian Henriques eventually make it a small hut with a door made of beads. You force the door open, revealing a sign that says, The Seer's Hut.")
sleep(delay)
print("Australian Henriques: What is this place? It looks like the route to the underworld.")
sleep(delay)
print("King Kong: You'll see who lives here soon enough. Now, allow me to call him.")
sleep(delay)
print("Narrator: You draw a pentagram in the sand, at which point the Seer stumbles out of the shadows and looks right into Australian Henriques' eyes.")
sleep(delay)
print("Australian Henriques: Crikey. That's one damn creepy Yank.")
sleep(delay)
print("Lil Nas X (Seer): Well... if it isn't King Kong. Come down to this old town road again, eh? I can't help a fugitive like you, sorry.")
sleep(delay)
print("King Kong: You can help me. We both know you can. Australian Henriques and I need to bring about the drums of liberation.")
sleep(delay)
print("Lil Nas X: Still talking in riddles, eh?")
sleep(delay)
print("King Kong: You know exactly what I mean.")
sleep(delay)
print("Lil Nas X: I suppose I do. Well, if you want my help, you'll have to beat me in combat. My magic orb, it's for the champions.")
sleep(delay)
print("King Kong: If you want a challenge, then bring it. Your skills are the least of my worries.")
sleep(delay)
print("Lil Nas X: Eh? I haven't lost since I began, yeah.")
sleep(delay)
print(f"Narrator: In Bananaland, when you accept a challenge from an opponent, their stats will flash on your screen. Furthermore, you currently have {health} health. You must gamble a certain amount of health, and you will either lose it or absorb your opponents health. Your opponent will automatically gamble the same amount of health as you.")
sleep(delay)
gamble = int(input("Narrator: How much health would you like to gamble? Lil Nas X has 50 health, so I recommend you gamble 50, so you don't have to play him again. Enter health here: "))
sleep(delay)
print(Lil_Nas_X)
sleep(delay)

blackjack()
while players_sum > 21:
    print("Lil Nas X: Still undefeated, yeah, cause I haven't lost since I began. You can keep trying to beat me, but you won't be able to.")
    new_health = health - gamble
    if new_health <= 0:
        print("You are out of health, and your game has ended.")
        break
    blackjack()
while players_sum < opponents_sum and opponents_sum < 21:
    print("Lil Nas X: Still undefeated, yeah, cause I haven't lost since I began. You can keep trying to beat me, but you won't be able to.")
    new_health = health - gamble
    if new_health <= 0:
        print("You are out of health, and your game has ended.")
        break
    blackjack()
if opponents_sum > 21:
    print("Lil Nas X: How could you have possibly defeated me, when I haven't lost since I began, yeah? I guess I'll help you now that you have proven yourself worthy.")

print(f"Narrator: Your health is now {new_health}.")