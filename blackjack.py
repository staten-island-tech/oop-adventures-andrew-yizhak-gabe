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
    def __init__(self,cardValue,cardDrawn,totalValue,gambledHealth,wl):
        self.cardValue=cardValue
        self.cardrawn=cardDrawn
        self.totalValue=totalValue
        self.gambledHealth=gambledHealth
        self.wl=wl
def card():
    return game

c=card()
    #cardValue represents the value of the cards. cardDrawn will allow us too
def blackjack():
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

    #THE GAME   
    c.gambledHealth=input('input how much health you want too gamble:')
    draw('Your faceup',players_hand)
    draw('Your facedown',players_hand)
    sleep(delay) #the two lines above will tell the player what their hand is
    opponents_hand.append(random.choice(cards))
    draw("Your opponent has one facedown card, and their faceup",opponents_hand) #Opponents hand
    sleep(delay)
    calculate(players_hand)
    player_value=c.totalValue
    calculate(opponents_hand)
    opponent_value=c.totalValue

    hit=input('Do you want to hit, or stand? |HIT/STAND| ').upper()
    while hit=='HIT':
        draw('Your new',players_hand)
        calculate(players_hand)
        player_value=c.totalValue
        print(player_value)
        if player_value<=21:
            hit=input('Do you want to hit, or stand? |HIT/STAND| ').upper() #ERROR WITH BUSTING, MAKE SURE TO FIX
        else: 
            break

    if player_value<=21:
        print('OK, let\'s see what cards the dealer has.')
        while opponent_value<player_value:
            print(opponents_hand)
            print(players_hand)
            draw('Your opponents new card',opponents_hand)
            calculate(opponents_hand)
            opponent_value=c.totalValue
    
    #win/loss 

    if player_value>21 or (opponent_value>player_value and opponent_value<=21):
        c.wl='loss' 
    elif player_value==opponent_value:
        c.wl='tie'
    else:
        c.wl='win'
    return(c.wl,c.gambledHealth)

blackjack()
print(c.wl, c.gambledHealth)
