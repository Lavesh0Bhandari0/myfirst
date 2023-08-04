# Closure is a function having access to the scope of its parent function even after the parent function has returned.


def parent_function(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left. ")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left. ")
        else:
            print("\n" + person + " is out of coins. ")

    return play_game


lavesh = parent_function("Lavesh", 3)
# look at it as creating an instance of the nestd functions which has the speciality of acessing the parent function elements.
sejal = parent_function("Sejal", 5)

lavesh()
lavesh()

sejal()
lavesh()
