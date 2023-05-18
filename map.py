import money
from time import sleep
health = 0
skip_a_fight = 0
badges = []
inventory = []
maps = ["Potassium Palace", 'Ripe Ravine', 'Plaintain Plateau', 'Fruity Field']
map = "Potassium Palace"

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
        print("You bath in the pools of the Potassium Pool")
        sleep(2)
        print("As a result, your health has increased by 15!")

if map == "Ripe Ravine":
    decision = input("Where would you like to travel?: Store, Talk to Banana Caveman, Fight the Miniboss, Regular Fight, Healing Spot")
if map == "Plaintain Plateau":
    decision = input("Where would you like to travel?: Store, Talk to Banana Merchant, Fight the Miniboss, Regular Fight, Healing Spot")
if map == "Fruity Field":
    decision = input("Where would you like to travel?: Store, Talk to Banana Banana, Fight the Miniboss, Regular Fight, Healing Spot")