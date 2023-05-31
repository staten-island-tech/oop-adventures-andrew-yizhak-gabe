import random
from time import sleep

players_hand = [11,11,11,11,10,7]
opponents_hand = []
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
Tens=['10','Jack','Queen','King']
suits = ["Michael Whalen", "Gabriel Liberov", "Izzy Zoltan", "Andrew Rosini"]
delay=1
player_value=0
opponent_value=0

class game(): 
    def __init__(self,cardValue,cardDrawn,totalValue):
        self.cardValue=cardValue
        self.cardrawn=cardDrawn
        self.totalValue=totalValue
def card():
    return game

c=card()
"""

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
"""
def calculate(hand): 
     c.totalValue=0
     if 11 not in hand:
          c.totalValue=sum(hand)
          print(c.totalValue) #DELETE ONCE TESTING IS OVER
          return c.totalValue
     else:
        ace=0
        for cards in range(len(hand)):
             if hand[cards]!=11:
                c.totalValue+=hand[cards]
             if hand[cards]==11: 
                 ace+=1      
        for cards in range(len(hand)):
            if hand[cards]==11:
                if c.totalValue>(11-ace):
                    c.totalValue+=1
                else:
                    c.totalValue+=11
                    c.totalValue    
        
        print(c.totalValue)
        return(c.totalValue)

calculate(players_hand)

player_value=c.totalValue
print(player_value)
