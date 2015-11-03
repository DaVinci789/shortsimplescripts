# Coin Toss v0.1 by DaVinci789
# Help this project on GitHub
# DaVinci789 / shortsimplescripts / python / cointosssuite.py
# Written in Python 3

import random
import os
import sys
# define lists for the coin side and events + outcomes
coin = ["heads", "tails"]
randevents = ["normal","rolling", "disappeared"]
randoutcomes = ["normal","stuck", "lost"]
game_list = ["Heads or Tails", "Heads or Tails Classic", "Debug it you nasty cheater!"]
gamenum = 0

def titlescreen():
    global ui
    global gamenum
    os.system('cls' if os.name == 'nt' else 'clear')

    print("                                             /$$$$$$            /$$                 /$$$$$$$$                                  /$$$$$$            /$$   /$$")
    print("                                            /$$__  $$          |__/                |__  $$__/                                 /$$__  $$          |__/  | $$")
    print("                                           | $$  \__/  /$$$$$$  /$$ /$$$$$$$          | $$  /$$$$$$   /$$$$$$$ /$$$$$$$      | $$  \__/ /$$   /$$ /$$ /$$$$$$    /$$$$$$")
    print("                                           | $$       /$$__  $$| $$| $$__  $$         | $$ /$$__  $$ /$$_____//$$_____/      |  $$$$$$ | $$  | $$| $$|_  $$_/   /$$__  $$")
    print("                                           | $$      | $$  \ $$| $$| $$  \ $$         | $$| $$  \ $$|  $$$$$$|  $$$$$$        \____  $$| $$  | $$| $$  | $$    | $$$$$$$$")
    print("                                           | $$    $$| $$  | $$| $$| $$  | $$         | $$| $$  | $$ \____  $$\____  $$       /$$  \ $$| $$  | $$| $$  | $$ /$$| $$_____/")
    print("                                           |  $$$$$$/|  $$$$$$/| $$| $$  | $$         | $$|  $$$$$$/ /$$$$$$$//$$$$$$$/      |  $$$$$$/|  $$$$$$/| $$  |  $$$$/|  $$$$$$$")
    print("                                            \______/  \______/ |__/|__/  |__/         |__/ \______/ |_______/|_______/        \______/  \______/ |__/   \___/   \_______/")

    print("\n\n\n\n\n\n\n\n\n\n1) List Games")
    print("2) Options")
    print("3) Help")
    print("4) Exit")
    while True:
        try:
            ui = int(input(": "))
            if ui == 1:
                for name in game_list:
                    print(name)

                while True:
                    try:
                        ui = int(input("Please enter the # of your game (0 to exit): "))
                        if ui == 1:
                            gamenum = 1
                            main()
                        elif ui == 2:
                            gamenum = 2
                            main1()
                        elif ui == 3:
                            gamenum = 3
                            main2()
                        elif ui == 0:
                            titlescreen()
                        else:
                            print("Game not found")
                        break
                    except ValueError:
                        print("Not a #")

            elif ui == 2:
                print("That option is not avalible at this moment")
                titlescreen()
            elif ui == 3:
                print("This is a set of games based on random luck game of flipping a coin.")
                print("v0.01")
            else:
                print("Not a possible answer")
                os.system('cls' if os.name == 'nt' else 'clear')
                titlescreen()
        except ValueError:
            print("Not a valid choice")

# main function that every outcome returns to
def main():
    global ui
    global side
    global gamenum
    ui = input("Heads or Tails?: ").lower()
    side = random.choice(coin)
    print(side)
    # start random outcomes
    startrand = random.randint(0 , 52)
    if gamenum == 0 or gamenum == 2:
        if startrand >= 39:
            randevents_events()
        # goto normal ending if not equal
        else:
            finaloutcome(0)

# random events chooser
def randevents_events():
    seed = 0
    seed = random.randint(0, 100)
    # make choosing a 25% chance look fancy
    if seed >= 50:
        seed = seed % 2
        if seed == 0:
            randevents_outcomes(1)
        else:
            # normie outcomes
            randevents_outcomes(0)
    # really special chance of 1/100
    elif seed == 100:
        randevents_outcomes(2)
    else:
        # another normie outcome
        randevents_outcomes(0)

# the function that actually chooses the outcome
def randevents_outcomes(event):
    outcome = random.randint(0, 8)
    for result in range(0, 2):
        if result == event:
            final = result + outcome
            finaloutcome(final)

# outcome finalizer
def finaloutcome(result):
    #ui = raw_input("Heads or Tails: ").lower()`
    global ui
    global side
    # start checking results
    if result == 0:
        # normal, normal
        if ui == side:
                print("The coin you threw landed back into your hand and produced",ui,".")
                print("You Win.")
                main()
        else:
            if ui == coin[0]:
                ui = coin[1]
                print("The coin you threw landed back into your hand and produced",ui,".")
                print("You Lost :(")
                main()
            else:
                print("The coin you threw landed back into your hand an produced heads .")
                print("You Lost :(")
                main()
    elif result == 1:
           # normal, stuck
           print("You threw the coin, but it somehow landed on its edge.")
           main()
    elif result == 2:
           # normal, lost
           print("You threw the coin, but it fell through a gap on the floor, luckily you had another and flipped that one instead, call it!")
           main()
    elif result == 3:
        if side == ui:
            # rolling, normal
            print("The coin bounces on the table, and rolls for a while before finally landing on",ui,".")
            print("You Win, whew.")
        else:
            if ui == "heads":
                print("The coin bounces and rolls before falling of the table. When you go and check on it it reveals tails")
                print("Arrgh! You Lose.")
                main()
    elif result == 4:
        # rolling, stuck
        print("The coin rolls for a while before finally stopping on its edge. What?!")
        print("Draw?")
        main()
    elif result == 5:
        # rolling, lost
        print("The coin you threw rolled in between two pieces of furniture. Sighing, you take out another one and throw that instead.")
        main()
    elif result == 6:
        # disappear, normal
        if side == ui:
            print("The coin you threw fell into a gap between time and space and disappeared for a moment before another alien coin falls into your hand.")
            print("When you make it out, it looks like",ui,".")
            print("Huh, weird, I guess you won anyway.")
        else:
            if side == heads:
                print("The coin you threw disappeared for a moment until it somehow smashed onto your table, fracturing it.")
                print("At least one side is still visable, and it says tails")
                print("A unique alien experience for 12 seconds and you still lost?!")
                main()
            else:
                print("The coin you threw disappeared for 12 seconds in the air before someone that looks like you throws a coin at you  and tells you that it landed on heads")
                print("Even your future self is sad.")
                print("Well, you lost.")
                main()
    elif result == 7:
        # disappeared, stuck
        print("The coin you threw landed in a gap between time and space, trapping it there for all eternity.")
        print("You try to see what side its on, but its stuck perpendicular to the floor.")
        print("Well its a draw.")
        main()
    elif result == 8:
        # disappeared, lost
        print("The coin you threw disappeared")
        print("That's all, you threw it and it disappeared in a flash of light.")
        print("Huh.")
        main()
    else:
        # out of bounds
        print("DEBUG ERROR: result IS OUT OF BOUNDS")
        main()
titlescreen()
#main()
