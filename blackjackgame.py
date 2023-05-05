import blackjack 
import random

playershand=[[],{'Card Value':0}]
opponentshand=[]
cardsdrawn=0
random.shuffle(blackjack.deck)

def draw(hand,x):
    global cardsdrawn

    if cardsdrawn==51:
        cardsdrawn=0
        random.shuffle(blackjack.deck)
    for cards in range(x):
        hand.append(blackjack.deck[cardsdrawn])
        cardsdrawn+=1

def cardvalue(hand,x):
    for i in x:
        if 'ace' not in hand[cardsdrawn]:
            hand[cardsdrawn]['Card Value']+=blackjack.deck[cardsdrawn]['Card Value']
            if hand[cardsdrawn]['']:
                pass
def game():
    global cardsdrawn
    cardsdrawn=0
    draw(playershand,2)
    
    print(f'Welcome to the blackjack BETA! Here, this is your starting hand! {playershand}')

    draw(opponentshand,2)
    drawmore=input(f'Your dealer has the {opponentshand[0]} and one facedown card. Do you want to draw? |Y/N|').upper()[0]

    while drawmore == 'Y':
        draw(playershand,1)
        

"""

            calculate card value (have fun calcing ace)

            if handvalue > 21: 
                print('you lose')
            else:
                ask user if they want to drawmore
        

 """
game()