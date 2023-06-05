import money
from time import sleep
health = 0
skip_a_fight = 0
badges = []
inventory = []
maps = ["Potassium Palace", 'Ripe Ravine', 'Plaintain Plateau', 'Fruity Field']
map = "Plaintain Plateau"

while map == "Potassium Palace":
    decision = input("Where would you like to travel?: Store, Talk to Banana King, Regular Fight, Healing Spot, I HATE POTASSIUM PALACE TAKE ME OUT OF HERE")
    if decision == "Store":
         economical_decision = input("State what you would like to purchase: Health, Skip-a-Fight, Potassium Palace Badge, Go Back")
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
                    economical_decision = input("State what you would like to purchase: Health, Skip-a-Fight, Potassium Palace Badge, Go Back")
        
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
                    economical_decision = input("State what you would like to purchase: Health, Skip-a-Fight, Potassium Palace Badge, Go Back")
        
            if economical_decision == "Potassium Palace Badge":
                if money.currency < 500:
                    print("Sorry Brokie! You can't buy this!")
                elif money.currency >= 500:
                    money.currency = money.currency - 500
                    print("Processing order...")
                    sleep(2)
                    print(f"Your purchase has been completed! New Balance: {money.currency} New Badge Unlocked: Potassium Palace Badge")
                    sleep(2)
                    economical_decision = input("State what you would like to purchase: Health, Skip-a-Fight, Potassium Palace Badge, Go Back")
    if decision == "Talk to Banana King":
        print("Entering the throne room of Banana King...")
        sleep(3)
        print('Banana King: "Welcome to my throne room you goofy monkey"')
        sleep(3)
        king_decision = input('Banana King: "Would you like a present from me...": Y/N')
        if king_decision == 'N':
            print('Banana King: "How could you reject my gift you stupid baboon! Leave my site at once!"')
            sleep(3)
            print("You have been kicked out of the throne room by the royal Banana guards AND have upset the Banana King. As a result, your health has decreased by 25 points!")
            sleep(4)
        if king_decision == 'Y':
            print('Banana King: "Good choice monkey. Here is a banana as memory of my generous Banana grace"')
            inventory.append("Banana King's Banana")
            sleep(2)
            print("Banana King's Banana has been added to your inventory!")
    if decision == "Healing Spot":
        print("You bathe in the pools of the Potassium Pool")
        health = health + 15 
        sleep(2)
        print("As a result, your health has increased by 15!")

while map == "Ripe Ravine":
    decision = input("Where would you like to travel?: Store, Talk to Banana Caveman, Fight the Miniboss, Regular Fight, Healing Spot")
    if decision == "Store":
         economical_decision = input("State what you would like to purchase: Health, Skip-a-Fight, Ripe Ravine Badge, Go Back")
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
                    economical_decision = input("State what you would like to purchase: Health, Skip-a-Fight, Ripe Ravine Badge, Go Back")
        
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
                    economical_decision = input("State what you would like to purchase: Health, Skip-a-Fight, Ripe Ravine Badge, Go Back")
        
            if economical_decision == "Ripe Ravine Badge":
                if money.currency < 500:
                    print("Sorry Brokie! You can't buy this!")
                elif money.currency >= 500:
                    money.currency = money.currency - 500
                    print("Processing order...")
                    sleep(2)
                    print(f"Your purchase has been completed! New Balance: {money.currency} New Badge Unlocked: Ripe Ravine Badge")
                    sleep(2)
                    economical_decision = input("State what you would like to purchase: Health, Skip-a-Fight, Ripe Ravine Badge, Go Back")
    if decision == "Healing Spot":
        print("You bathe in the pools of the Potassium Pool")
        health = health + 15 
        sleep(2)
        print("As a result, your health has increased by 15!")

    if decision == "Talk to Banana Caveman":
        print("Travelling to the Cave of Banana Caveman...")
        sleep(3)
        print('Banana Caveman: "Ooga Banana Booga, if it isn\'t the big monkey himself"')
        caveman_decision = input('Banana Caveman: "Would you like to give me money for no reason?" Y/N') 
        if caveman_decision == "Y":
            money.currency = money.currency - 1
            print('Banana Caveman: "Thanks. No reward though hahaha"')
            sleep(2)
        if caveman_decision == "N":
            print('Banana Caveman: "Alright whatever leave"')
            sleep(2)
while map == "Plaintain Plateau":
    decision = input("Where would you like to travel?: Store, Talk to Banana Merchant, Fight the Miniboss, Regular Fight, Healing Spot")
    if decision == "Store":
         economical_decision = input("State what you would like to purchase: Health, Skip-a-Fight, Plaintain Plateau Badge, Go Back")
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
                    economical_decision = input("State what you would like to purchase: Health, Skip-a-Fight, Plaintain Plateau Badge, Go Back")
        
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
                    economical_decision = input("State what you would like to purchase: Health, Skip-a-Fight, Plaintain Plateau Badge, Go Back")
        
            if economical_decision == "Plaintain Plateau Badge":
                if money.currency < 500:
                    print("Sorry Brokie! You can't buy this!")
                elif money.currency >= 500:
                    money.currency = money.currency - 500
                    print("Processing order...")
                    sleep(2)
                    print(f"Your purchase has been completed! New Balance: {money.currency} New Badge Unlocked: Plaintain Plateau Badge")
                    sleep(2)
                    economical_decision = input("State what you would like to purchase: Health, Skip-a-Fight, Plaintain Plateau Badge, Go Back")
    
    if decision == "Talk to Banana Merchant":
        print("Entering the tent of the Banana Merchant...")
        sleep(3)
        print('Banana Merchant: "Welcome to my tent you goofy monkey"')
        sleep(2)
        merchant_decision = input('Banana Merchant: "I have been searching years for the legendary Banana King\'s Banana. Have you happen to come across this beauty?": Y/N')
        if merchant_decision == 'Y':
            if "Banana King's Banana" in inventory:
                inventory.remove("Banana King's Banana")
                print("Wow! Thank you monkey! I am a happy Banana Merchant now!")
            else:
                print('Banana Merchant: "LIAR! Get out of my sight you monkey!"')
                sleep(2)
                print('You walk out of the tent sad that you could not fufill the request of the Banana Merchant.')
        if merchant_decision == 'N':
            print('Banana Merchant: "Understandable, have a nice day monkey"')
            sleep(2)
            print('You walk out of the tent sad that you could not fufill the request of the Banana Merchant.')
            sleep(3)  
    if decision == "Healing Spot":
        print("You bathe in the pools of the Potassium Pool")
        health = health + 15 
        sleep(2)
        print("As a result, your health has increased by 15!") 


while map == "Fruity Field":
    decision = input("Where would you like to travel?: Store, Talk to Banana Banana, Fight the Miniboss, Regular Fight, Healing Spot")
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
    if decision == "Healing Spot":
        print("You bathe in the pools of the Potassium Pool")
        health = health + 15 
        sleep(2)
        print("As a result, your health has increased by 15!")