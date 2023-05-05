import blackjack 
import random

playershand=[]
opponentshand=[]
cardsdrawn=0
random.shuffle(blackjack.deck)

def draw(card,x):
    
    if cardsdrawn==51:
        cardsdrawn=0
        random.shuffle(blackjack.deck)
    for cards in range(x):
        card.append(blackjack.deck[cardsdrawn])
        cardsdrawn+=1
        
def game():
    global cardsdrawn
    cardsdrawn=0
    draw(playershand,2)
    print(f'Welcome to the blackjack BETA! Here, this is your starting hand! {playershand}')

    draw(opponentshand,2)
    drawmore=input(f'Your dealer has the {opponentshand[0]} and one facedown card. Do you want to draw? |Y/N|').upper()[0]

    while drawmore == 'Y':
        """
        calculate card value (have fun calcing ace)

        if handvalue > 21: 
            print('you lose')
        else:
            ask user if they want to drawmore
        

        """
game()