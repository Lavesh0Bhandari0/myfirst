import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = "True"
while playagain:
    """
    print(RPS(2))
    print(RPS.ROCK)
    print(RPS["ROCK"])
    print(RPS.ROCK.value)
    sys.exit()"""
    playerchoice = input(
        " \nEnter... \n 1 for Rock \n 2 for Paper \n 3 for Scissors: \n\n"
    )
    playerchoice = int(playerchoice)
    if playerchoice < 1 or playerchoice > 3:
        sys.exit("You must enter 1, 2, or 3.")

    computerchoice = random.choice("123")
    computerchoice = int(computerchoice)
    print(" \nYou chose " + str(RPS(playerchoice)).replace("RPS.", "") + " .")
    print(" \n Python chose " + str(RPS(computerchoice)).replace("RPS.", "") + " .")

    if playerchoice == 1 and computerchoice == 3:
        print("You Win!")
    elif playerchoice == 2 and computerchoice == 1:
        print("You Win!")
    elif playerchoice == 3 and computerchoice == 2:
        print("You Win!")
    elif playerchoice == computerchoice:
        print("Tie game")
    else:
        print("Python Wins!")
    check = input("input O to play and X to quit.").lower()
    if check == "x":
        break
