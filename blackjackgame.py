import blackjack 
import random

playershand=[]
opponentshand=[]
cardsdrawn=0
random.shuffle(blackjack.deck)

def draw(card,x,cardsdrawn):
    if cardsdrawn==51:
        cardsdrawn=0
        random.shuffle(blackjack.deck)
    for cards in range(x):
        card.append(blackjack(cardsdrawn))
        cardsdrawn+=1

draw(playershand,2,cardsdrawn)
print('Welcome to the blackjack BETA! Here, this is your starting hand!' + {playershand})

