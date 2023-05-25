import random
from time import sleep

players_hand = []
opponents_hand = []
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
Tens=['10','Jack','Queen','King']
suits = ["Michael Whalen", "Gabriel Liberov", "Izzy Zoltan", "Andrew Rosini"]
delay=1
player_value=0
opponent_value=0


class game(): 
    def __init__(self,cardValue,cardDrawn):
        self.cardValue=cardValue
        self.cardrawn=cardDrawn
        
def card():
    return game

c=card()
#cardValue represents the value of the cards. cardDrawn will allow us too
def draw(facing,hand):
    c.cardValue = random.choice(cards)
    if c.cardValue == 10:
        c.cardDrawn=(f"{facing} card is the {random.choice(Tens)} of {random.choice(suits)}.")
    elif c.cardValue < 10:
        c.cardDrawn=(f"{facing} card is the {c.cardValue} of {random.choice(suits)}.")
    elif c.cardValue == 11:
            c.cardDrawn=(f"{facing} card is the ace of {random.choice(suits)}.")
    hand.append(c.cardValue)
    print(c.cardDrawn)
    print(hand)#DELETE ONCE TESTING IS OVER 

def calculate(hand,value):
     if 11 not in hand:
          value=sum(hand)
          print(value) #DELETE ONCE TESTING IS OVER
          return value
     else:
        value=0
        for cards in range(len(hand)):
             if hand[cards]!=11:
                value+=hand[cards]
        for cards in range(len(hand)):
            if hand[cards]==11:
                if value>10:
                    value+=1
                else:
                    value+=11
        print(value) #DELETE ONCE TESTING IS OVER
        return value 

#THE GAME   
draw('Your faceup',players_hand)
draw('Your facedown',players_hand)
sleep(delay) #the two lines above will tell the player what their hand is
opponents_hand.append(random.choice(cards))
draw("Your opponent has one facedown card, and their faceup",opponents_hand) #Opponents hand
sleep(delay)
calculate(players_hand,player_value)
calculate(opponents_hand,opponent_value)

hit=input('Do you want to hit, or stand? |HIT/STAND| ').upper()
while hit=='HIT':
    draw('Your new',players_hand)
    calculate(players_hand,player_value)
    print(player_value)
    if player_value>21:
        hit='STAND'
        break
    hit=input('Do you want to hit, or stand? |HIT/STAND| ').upper() #ERROR WITH BUSTING, MAKE SURE TO FIX

"""
hit_or_stand = input("Would you like to hit or stand? Hit/Stand: ")
while hit_or_stand == "Hit":
    new_card=game.card('new card',cardValue,players_hand)
    
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
    cardValue = random.choice(cards)
    if cardValue == 10:
        new_card = (f"Your new card is the {random.choice(Tens)} of {random.choice(suits)}.")
    elif cardValue < 10:
        new_card = (f"Your new card is the {cardValue} of {random.choice(suits)}.")
    elif cardValue == 11:
        new_card = (f"Your new card is the ace of {random.choice(suits)}.")
        if sum(players_hand) + 11 > 21:
            cardValue = 1
        elif sum(players_hand) + 11 < 21:
            cardValue = input("Would you like your ace to be valued as a 1 or 11? |1|11|: ")
            if cardValue == "1":
                cardValue = 1
            elif cardValue == "11":
                cardValue = 11
    opponents_hand.append(cardValue)
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
"""