# f-strings or format strings
person = "Lavesh"
coins = 5

message = "\n{} has {} coins left.".format(person, coins)
print(message)
message2 = "\n{1} has {0} coins left".format(coins, person)
print(message2)
message3 = "\n{persons} has {coin} coins left.".format(coin=coins, persons=person)
print(message3)
player = {"persons": "lavesh", "coin": 5}
message4 = "\n{persons} has {coin} coins left.".format(**player)
print(message4)

message5 = f"\n{person} has {coins} coins left"
print(message5)
message6 = f"\n{person.lower()} has {10*2} coins left"
print(message6)
message7 = f"\n{player['persons']} has {10*2} coins left"
print(message7)
