import random
from time import sleep


cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
Tens=['10','Jack','Queen','King']
suits = ["Michael Whalen", "Gabriel Liberov", "Izzy Zoltan", "Andrew Rosini"]
delay=1
player_value=0
opponent_value=0

class game(): 
    def __init__(self,cardValue,cardDrawn,totalValue,wl):
        self.cardValue=cardValue
        self.cardrawn=cardDrawn
        self.totalValue=totalValue
        self.wl=wl
def card():
    return game

c=card() 
def blackjack():
    players_hand = []
    opponents_hand = []
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

    def calculate(hand): 
        c.totalValue=0
        if 11 not in hand:
            c.totalValue=sum(hand)
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

            return(c.totalValue)#THE GAME   
            

    draw('Your faceup',players_hand)
    draw('Your facedown',players_hand)
    sleep(delay) #the two lines above will tell the player what their hand is
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
        if player_value<=21:
            hit=input('Do you want to hit, or stand? |HIT/STAND| ').upper() #ERROR WITH BUSTING, MAKE SURE TO FIX
        else: 
            break

    if player_value<=21:
        print('OK, let\'s see what cards the dealer has.')
        draw('Your opponent\'s facedown',opponents_hand)
        while opponent_value<player_value:
            
            sleep(delay)
            draw('Your opponent draws another card. Their new',opponents_hand)   
            calculate(opponents_hand)
            print(f'Your opponent\'s hand is valued at {c.totalValue}. ')
            sleep(delay)
            opponent_value=c.totalValue
    else: 
        print('Oh no! You busted.')#win/loss 

    if player_value>21:
        c.wl='loss' 
    elif (opponent_value>player_value and opponent_value<=21):
        c.wl='loss'
    elif player_value==opponent_value:
        c.wl='tie'
    else:
        c.wl='win'
    return(c.wl)