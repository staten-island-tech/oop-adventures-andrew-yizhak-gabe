import blackjack 
import random

playershand=[[],{'Card Value':0}]
opponentshand=[]
random.shuffle(blackjack.deck)

def draw(hand,x):

    random.shuffle(blackjack.deck)
    for cards in range(x):
        
        hand[0].append(blackjack.deck[0])
        if 'Ace' not in blackjack.deck[0].values():

            hand[1]['Card Value'] += blackjack.deck[0].values()

        else: 
         
            hand.append('and an Ace.')
        
def calculate(hand):
    
    if len(hand)==3:
        if 'Card Value' > 20:
            print('Bust!')
            global drawmore
            drawmore=='N'
            global youlose
            youlose=True 
    else:
        if 'Card Value' > 21:
            drawmore='N'
            youlose=True

def Pass(hand):
    if len(hand) == 3:
        if (hand[1]['Card Value']+11)>21:
            hand[1]['Card Value']+=1
        else: hand[1]['Card Value']+=11
    hand.remove('And an Ace')

def game():
    playershand=[[],{'Card Value':0}]
    draw(playershand,2)

    print(f'Welcome to the blackjack BETA! Here, this is your starting hand! {playershand[0]}')

    draw(opponentshand,2)
    drawmore=input(f'Your dealer has the {opponentshand[0]} and one facedown card. Do you want to draw? |Y/N|').upper()[0]

    while drawmore == 'Y':
        calculate(playershand)
        draw(playershand,1)

    if youlose==True:
        print('You lost! do you want to retry?')
    else: 
        Pass(playershand)

game()

