import blackjack 
import random

playershand=[]
opponentshand=[]
cardsdrawn=0
random.shuffle(blackjack)

def draw(card,x):
    if cardsdrawn==51:
        cardsdrawn=0
        random.shuffle(blackjack)
    for cards in range(x):
        card.append(blackjack(cardsdrawn))
        cardsdrawn+=1

draw(playershand,2)
print('Welcome to the blackjack BETA! Here, this is your starting hand!' + {playershand})

