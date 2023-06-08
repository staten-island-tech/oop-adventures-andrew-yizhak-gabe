from time import sleep
import blackjack
delay=3


def fight(players_health,opponent,loss,tie,win,gameover):
    print(f"Narrator: You are fighting {opponent.name}. {opponent.name} has {opponent.health} hp. Good luck!")
    play=True
    while play==True:

        gambledHealth=int(input(f"Narrator: How much health would you like to gamble on the fight? You currently have {players_health} health: "))
        while gambledHealth>players_health:
             gambledHealth=int(input(f"Narrator:Sorry, please gamble an amount that is less than or equal to your current health. \n How much health would you like to gamble on the fight? You currently have {players_health} health: "))
        blackjack.blackjack()
        if blackjack.c.wl=='loss':
            print(loss)
            players_health-=gambledHealth
        
        elif blackjack.c.wl=='tie':
            print(tie)
        else:

            opponent.health-=gambledHealth     
            players_health+=round(gambledHealth/2)
            print(win)
            sleep(delay)
            print(f"Narrator: Your opponent is now at {opponent.health} health.")
                
            if opponent.health < 1:
                    print(gameover)
                    play=False
                    return players_health
            
            elif players_health<1:
                print('Narrator: You may have lost, but there\'s always hope. Come back King Kong, too bring about the drums of liberation.')
                players_health=100
                print('Try again:')