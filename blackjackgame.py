import blackjack 
import random

playershand=[]
opponentshand=[]
cardsdrawn=0
random.shuffle(blackjack.deck)

def draw(card,x):
    global cardsdrawn

    if cardsdrawn==51:
        cardsdrawn=0
        random.shuffle(blackjack.deck)
    for cards in range(x):
        card.append(blackjack.deck[cardsdrawn])
        cardsdrawn+=1

draw(playershand,2)
print(f'Welcome to the blackjack BETA! Here, this is your starting hand! {playershand}')


