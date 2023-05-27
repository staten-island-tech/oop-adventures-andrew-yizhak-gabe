from time import sleep
from classes import Lil_Nas_X
from classes import henchman
from classes import enforcer
from itertools import repeat
count = []
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
print(f"Narrator: In Bananaland, when you accept a challenge from an opponent, their stats will flash on your screen. Furthermore, you currently have {health} health. You must gamble a certain amount of health, and you will either lose it or absorb your opponents health. Your opponent will automatically gamble the same amount of health as you, unless they are a hit opponent, who you will have to defeat once for each number of hits.")
sleep(delay)
gamble = 10
print("Narrator: Normally, you will have to gamble a certain amount of health to lower an enemy. However, Lil Nas X is a special hit boss, so your gamble will automatically be 10 per 1 hit.")
sleep(delay)
print(Lil_Nas_X)
sleep(delay)

blackjack()
while players_sum > 21:
    print("Lil Nas X: Still undefeated, yeah, cause I haven't lost since I began. You can keep trying to beat me, but you won't be able to.")
    new_health = health - gamble
    count.append(1)
    if new_health <= 0:
        print("You are out of health, and your game has ended.")
        break
    blackjack()
while players_sum < opponents_sum and opponents_sum < 21:
    print("Lil Nas X: Still undefeated, yeah, cause I haven't lost since I began. You can keep trying to beat me, but you won't be able to.")
    new_health = health - gamble
    count.append(1)
    if new_health <= 0:
        print("You are out of health, and your game has ended.")
        break
    blackjack()
if opponents_sum > 21:
    print("Lil Nas X: How could you have possibly defeated me, when I haven't lost since I began, yeah? I guess I'll help you now that you have proven yourself worthy.")
    if count != 0:
        new_health = health - ((len(count)) * gamble)
    elif count == 0:
        new_health = health

health == new_health
count.clear()

print(f"Narrator: Your health is now {health}. You will need to survive the rest of this level with {health} health.")
sleep(delay)
print("Lil Nas X: Okay, so you said you need to bring about the drums of liberation. How exactly do you plan to take down the bird mafia?")
sleep(delay)
print("King Kong: Well, after extensive research and some help from Australian Henriques, who went undercover into the Bird Mafia, I have determined that there are five main leaders that I need to take out to make the Bird Mafia collapse from within.")
sleep(delay)
print("Lil Nas X: Ah, yes. Well, to even make it to the Bird Mafia leaders, you will need to make your presence known. For that, I recommend you go talk to Bobby Hill. He moves around a lot, but rumors are that he is currently residing in NewNana.")
sleep(delay)
print("King Kong: Thank you. I need to go pay this Bobby Hill a visit.")
sleep(delay)
print("Australian Henriques: See ya later, yank.")
sleep(delay)
print("Narrator: You and Australian Henriques stroll out of the Seer's house, but when you get a few blocks away, a short, stocky man beings approaching you. He is carrying a baton made out of a long, powerful looking feather.")
sleep(delay)
print("Australian Henriques: Kong... get behind me...")
sleep(delay)
print("Narrator: You dart behind Australian Henriques just as the stocky man reaches you, at which point you realize he is local law enforcement.")
sleep(delay)
print("Henchman: Hello boys, how are you today?")
sleep(delay)
print("Australian Henriques: Alright, but these damn Yanks are acting crazy.")
sleep(delay)
print("Narrator: At this point, the henchman holds up a picture of King Kong.")
sleep(delay)
print("Henchman: You boys wouldn't have happened to see this monkey around here, have you? Because he is wanted by Bird Mafia.")
sleep(delay)
print("King Kong: I'm an ape, damn it!")
sleep(delay)
print("Narrator: You grab the henchman by his uniform, chucking him across the way. However, he is unfazed as you didn't damage him using the power of blackjack.")
sleep(delay)
print("Narrator: The henchman then pulls out his walkie talkie and calls for backup, before advancing on you himself.")
sleep(delay)
print("Henchman: Kong... you are going to regret pulling that maneuver.")
sleep(delay)
print("King Kong: Squawk, squawk then birdie... let's do this.")
sleep(delay)
print(henchman)
sleep(delay)
gamble = int(input(f"Narrator: How much health would you like to gamble on the fight? You currently have {health} health: "))

def henchman_fight():
    blackjack()
    while players_sum > 21:
        print("Narrator: The henchman wacks you with his baton, grinning as he slowly defeats you.")
        new_health = health - gamble
        count.append(1)
        if new_health <= 0:
            print("You are out of health, and your game has ended.")
            break
        blackjack()
    while players_sum < opponents_sum and opponents_sum < 21:
        print("Narrator: The henchman wacks you with his baton, grinning as he slowly defeats you.")
        new_health = health - gamble
        count.append(1)
        if new_health <= 0:
            print("You are out of health, and your game has ended.")
            break
        blackjack()
    if opponents_sum > 21:
        if count != 0:
            new_health = health - ((len(count)) * gamble)
        elif count == 0:
            new_health = health
        henchman_health = 30 - gamble
        if henchman_health <= 0:
            print("King Kong: Bam. Scumbag down.")
            sleep(delay)
            return health and new_health
        elif henchman_health > 0:
            print("Australian Henriques: Watch out, this Yank's coming back for more.")
            sleep(delay)
            print(f"The henchman you are facing is now on {henchman_health}.")
henchman_fight()

#Next up: force the henchman fight to repeat, make fight scene, make boss fight, then done with Fruity Fields.#