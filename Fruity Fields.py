from time import sleep
from classes import Lil_Nas_X
delay = 3

"""print("Narrator: You stroll out of the bar, eventually making your way to the neighborhood of Fruity Fields. There, you run into your sidekick, Australian Henriques.")
sleep(delay)
print("Australian Henriques: Bloody Yanks! I don't know why you're back here in Bananaland, with your bounty and all, but you should go.")
sleep(delay)
print("King Kong: Never mind that, Australian Henriques. Walk with me, there's someone I want you to meet.")
sleep(delay)
print("Narrator: The pair stroll on, passing signs of the dreadful Bird Mafia, the ones who put the bounty on you, all the way.")
sleep(delay)
print("Narrator: Together, you and Australian Henriques eventually make it a small hut with a door made of beads. You force the door open, revealing a sign that says, The Seer's Hut.")
sleep(delay)
print("Australian Henriques: What is this place? It looks like the route to the underworld.")
sleep(delay)
print("King Kong: You'll see who lives here soon enough. Now, allow me to call him.")
sleep(delay)
print("Narrator: You draw a pentagram in the sand, at which point the Seer stumbles out of the shadows and looks right into Australian Henriques' eyes.")
sleep(delay)
print("Australian Henriques: Crikey. That's one damn creepy Yank.")
sleep(delay)
print("Lil Nas X (Seer): Well... if it isn't King Kong. Come down to this old town road again, eh? I can't help a fugitive like you, sorry.")
sleep(delay)
print("King Kong: You can help me. We both know you can. Australian Henriques and I need to bring about the drums of liberation.")
sleep(delay)
print("Lil Nas X: Still talking in riddles, eh?")
sleep(delay)
print("King Kong: You know exactly what I mean.")
sleep(delay)
print("Lil Nas X: I suppose I do. Well, if you want my help, you'll have to beat me in combat. My magic orb, it's for the champions.")
sleep(delay)
print("King Kong: If you want a challenge, then bring it. Your skills are the least of my worries.")
sleep(delay)
print("Lil Nas X: Eh? I haven't lost since I began, yeah.")
sleep(delay)
print("Narrator: In Bananaland, when you accept a challenge from an opponent, their stats will flash on your screen.")
sleep(delay)
print(Lil_Nas_X)
sleep(delay)"""

def win_or_loss():
    placeholder = 0.1
    while placeholder != 0:
        from blackjack import blackjack
        from blackjack import win_or_loss
        player_win = win_or_loss
        if player_win == True:
            print("Lil Nas X: How could you possibly have defeated me, when I haven't lost since I began, yeah?")
            sleep(delay)
            print("Lil Nas X: I guess this is the end, yeah, so I'll help you now, eh?")
            sleep(delay)
            break
        elif player_win == False:
            print("Lil Nas X: Still haven't lost since I began, yeah, never say that it's the end, yeah.")
            sleep(delay)
            print("Lil Nas X: Try to beat me again, there's no way you can.")
            blackjack()
            player_win = win_or_loss
            print(player_win)
win_or_loss()