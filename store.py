import money
from time import sleep
health = 0
skip_a_fight = 0
badges = []
inventory = []
maps = ["Potassium Palace", 'Ripe Ravine', 'Plaintain Plateau', 'Fruity Field']
map = "Plaintain Plateau"


while map == "Fruity Field":
    decision = input("Where would you like to travel?: Store, Talk to Banana Banana")
    if decision == "Store":
         economical_decision = input("State what you would like to purchase: Health, Skip-a-Fight, Fruity Field Badge, Go Back")
    while decision == "Store":
    
        if economical_decision == "Go Back":
            leave = input("Are you sure you want to leave?: Y/N")
            if leave == "Y":
                print("You probably can't afford anything Brokie haha")
                sleep(2)
                break

        while economical_decision != "Go Back":
            if economical_decision == 'Health':
                if money.currency < 50:
                    print("Sorry Brokie! You can't buy this!")
                    sleep(2)
                elif money.currency >= 50:
                    health = health + 1
                    money.currency = money.currency - 50
                    print("Processing order...") 
                    sleep(2)
                    print(f"Your purchase has been completed! New Balance: {money.currency} New Health: {health}")
                    sleep(2)
                    economical_decision = input("State what you would like to purchase: Health, Skip-a-Fight, Fruity Field Badge, Go Back")
        
            if economical_decision == "Skip-a-Fight":
                if money.currency < 200:
                    print("Sorry Brokie! You can't buy this!")
                    sleep(2)
                elif money.currency >= 200:
                    skip_a_fight = skip_a_fight + 1 
                    money.currency = money.currency - 200
                    print("Processing order...")
                    sleep(2)
                    print(f"Your purchase has been completed! New Balance: {money.currency} New Skip-a-Fight Count: {skip_a_fight}")
                    sleep(2)
                    economical_decision = input("State what you would like to purchase: Health, Skip-a-Fight, Fruity Field Badge, Go Back")
        
            if economical_decision == "Fruity Field Badge":
                if money.currency < 500:
                    print("Sorry Brokie! You can't buy this!")
                elif money.currency >= 500:
                    money.currency = money.currency - 500
                    print("Processing order...")
                    sleep(2)
                    print(f"Your purchase has been completed! New Balance: {money.currency} New Badge Unlocked: Fruity Field Badge")
                    sleep(2)
                    economical_decision = input("State what you would like to purchase: Health, Skip-a-Fight, Fruity Field Badge, Go Back")
    if decision == "Talk to Banana Banana":
        print("Visiting Banana the Banana...")
        sleep(2)
        print('Banana Banana: "Hello good sir monkey! I know you like bananas, but please don\'t eat me!"')
        banana_decision = input("Follow Your Instincts? (WARNING YOU WILL REGRET IT): Y/N")
        if banana_decision == 'Y':
            health = 0
            print('You died! Thanks for playing King Kong\'s Greatest Ace! Do you feel proud of yourself that you ate the poor banana?')
            sleep(2)
            print('Signing off!')
            sleep(2)
        if banana_decision == 'N':
            health = health + 25
            print('Banana Banana: "Good choice sir monkey. You would have definitely regretted that decision. Have a reward of +25 Health!')
            sleep(2)
            print(f"New Health: {health}")