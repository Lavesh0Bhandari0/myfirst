# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# value = 1
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)

# else:
#     print("value is now equal to  " + str(value))

names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)

# for x in "Mississipi":
#     print(x)

for x in names:
    if x == "Sara":
        break
    print(x)

for x in range(0, 150, 15):
    print(x)
else:
    print("Glad that is over")

name = ["Lavesh", "Saket", "Ayush"]
actions = ["Runs", "Beats", "Sleeps"]

for x in name:
    for y in actions:
        print(x + " " + y)
