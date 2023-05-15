import money
from time import sleep
health = 0
map = ["Potassium Palace", 'Ripe Ravine', 'Plaintain Plateau', 'Fruity Field']
if map == "Potassium Palace":
    decision = input("Where would you like to travel?: Store, Talk to Banana King, Fight the Miniboss, Regular Fight, Healing Spot")
    if decision == "Store":
        economical_decision = input("Health", "Skip-a-Fight", "Potassium Palace Badge, Return Back") 
        if economical_decision == 'Health':
            if money.currency < 50:
                print("Sorry Brokie! You can't buy this!")
                sleep(2)
            elif money.currency >= 50:
                health = health + 1
                money.currency = money.currency - 50 
                sleep(2)
                print(f"Your purchase has been completed! New Balance: {money.currency}")
if map == "Ripe Ravine":
    decision = input("Where would you like to travel?: Store, Talk to Banana Caveman, Fight the Miniboss, Regular Fight, Healing Spot")
if map == "Plaintain Plateau":
    decision = input("Where would you like to travel?: Store, Talk to Banana Merchant, Fight the Miniboss, Regular Fight, Healing Spot")
if map == "Fruity Field":
    decision = input("Where would you like to travel?: Store, Talk to Banana Banana, Fight the Miniboss, Regular Fight, Healing Spot")