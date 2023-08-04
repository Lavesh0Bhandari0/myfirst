# Part 1. Practice Programm
from argparse import ArgumentParser, Namespace

import random

parser = ArgumentParser()
parser.add_argument("-n", "--name", help="Enter the name of the player.")
args: Namespace = parser.parse_args()
print(f"Welcome {args.name}")


def play_game():
    count = 0
    win = 0
    print("Enter your number!")
    x = int(input())
    if x not in [1, 2, 3]:
        print("Enter a valid number.")

    def game_one():
        t = int(random.choice("123"))
        nonlocal count
        count += 1
        print(f"\nGame count: {count}\nYou chose: {x}\nPython chose: {t}")
        if x == t:
            print("🎉You win")
            nonlocal win
            win += 1
        else:
            print("🐍 Python Wins")
        print(f"Winning percentage :{(win/count)*100}")

    return game_one


play = play_game()
play()
