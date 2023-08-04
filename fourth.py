# String data type
# literal assignment
first = "Lavesh"
last = "Bhandari"
""" print(type(first))
print(type(first) == str)
print(isinstance(first, str)) """
# Constructor Fucntion
""" pizza = str("Pepporoni")
print(type(first))
print(type(first) == str)
print(isinstance(pizza, str))
 """
# Concatenation
fullname = first + " " + last
print(fullname)
fullname += "!"
print(fullname)
# Casting a number to a String
decade = str(2000)
print(type(decade))

statement = "I like Linkin Park rock music from " + " decade " + decade
print(statement)

# Multiple Lines
multiline = """
Hey how are you?
I am good hope you are fine as well



                        All good at it.

"""
print(multiline)
# Escaping special character
sentence = " I'm back at work after a holiday. \tHey \n \n Where's this at \\located?"
print(sentence)

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)
print(multiline.title())
print(multiline.replace("well", "ok"))
print(multiline)


print(len(multiline))
multiline += "                               "
print(len(multiline))
multiline = "                       " + multiline
print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
print(len(multiline))

print("")
# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))
# String index values
print(first[0])
print(first[-1])
print(first[0:])

# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("h"))
# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))
# Numeric data types

# integer
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))
# Float types
gpa = 7.56
y = float(1.44)
print(type(gpa))
# Complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))


import math


print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a String to a number
zipcode = "100000"
zip_value = int(zipcode)
print(type(zip_value))
# Error if you attemp to cast incorrect data
zip_value + int("New York")
