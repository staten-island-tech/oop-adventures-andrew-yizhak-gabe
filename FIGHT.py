from time import sleep
import blackerjack
delay=3

def fight(opponent,loss,tie,win,gameover,opp0health):
    play=True
    while play==True:

        gambledHealth=int(input(f"Narrator: How much health would you like to gamble on the fight? You currently have {players_health} health: "))

        blackerjack.blackjack()
        if blackerjack.c.wl=='Loss':
            print(loss)
            players_health-=gambledHealth
        
        elif blackerjack.c.wl=='tie':
            print(tie)
        else:

            opponent.health-=gambledHealth     
            print(win)
            sleep(delay)
            print(f"Narrator: Your opponent is now at {opponent.health} health.")
                
            if opponent.health < 1:
                    print(gameover)
                    play=False
                    return players_health
            
            elif players_health<1:
                print(opp0health)
                players_health=100
                print('Try again:')