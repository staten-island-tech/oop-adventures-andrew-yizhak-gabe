from time import sleep
print("Narrator: Welcome to King Kong's Greatest Ace! The Bird Mafia has taken over Bananaland, and is using their corrupt values and powerful associates to poop on as many cars as possible. As King Kong, you will need to traverse the city and find a way to defeat the Bird Mafia once and for all. However, you will need to fight them not with guns, knives, or fists, but with knowledge, cunningness, and deception in a game of blackjack. Now, as you enter Bananaland for the first time, looking to create change, you walk into a local pub and find Big Bird standing there, serving customers.")
tutorial = input("Is this your first time playing? Y/N: ")
if tutorial == "Y":
    print("Narrator: Okay. As previously stated, you will need to defeat your enemies through the card game known as blackjack. Big Bird will now give you a brief explanation of how to play Blackjack.")
    sleep(10)
    print("Narrator: You now stumble into Big Bird's Bar, where Big Bird is waiting at the bar, ready to teach you how to play.")
    sleep(10)
    print("Big Bird: Hello! I will now teach you how to play blackjack. While blackjack is very simple, I will teach you the rules of the game and explain some easy strategies to make you better.")
    sleep(10)
    print("Big Bird: Blackjack is a simple game. Your goal is to get as close to a total of 21 without going over. The game will start with you and a dealer sitting across from one another. The dealer will give both you and him/herself a face-down card and a face-up card. You can now read your face down card.")
    sleep(10)
    print("Big Bird: After reading your two cards, add their values together, and determine whether or not you need more cards. If you are not sure what your total value is, remember that numbers 1-9 are taken at their face value and the number 10 and all face cards (jack, queen, and king) are worth 10. Aces are unique because they can be valued at either 1 OR 11 based on your situation. You get to decide.")
    sleep(10)
    print("Big Bird: A second or two after you read your cards, the dealer will ask you if you want to HIT or STAND. HIT means you will draw another card, and STAND means that you are done receiving cards. You can HIT as many times as you want, but if you go over a total of 21, you BUST and are automatically out.")
    sleep(10)
    print("Big Bird: Furthermore, if you STAND but have less total points than the dealer, you lose. Finally, if you immediately draw an ace and a jack, you get BLACKJACK and automatically win the round.")
    sleep(10)
    print("Big Bird: OK! You now have a basic idea of how blackjack works.")
    tutorial_game = input("Big Bird: Would you like to play a warmup round with me to make sure you understand the rules? Y/N: ")
    if tutorial_game == "Y":
        mode = "NORMAL"
        """Add in the blackjack function when it is ready."""
    elif tutorial_game == "N":
        mode = "HARD"
        print("Big Bird: That was very rude of you.")
elif tutorial == "N":
    tutorial_game = input("Big Bird: Would you like to play a warmup round with me to make sure you understand the rules? Y/N: ")
    if tutorial_game == "Y":
        mode = "NORMAL"
        """Add in the blackjack function when it is ready."""
    elif tutorial_game == "N":
        mode = "HARD"
        print("Big Bird: That was very rude of you.")