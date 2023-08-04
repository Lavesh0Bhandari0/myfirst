users = ["Dave", "John", "Sara"]
data = ["Dave", 24, True]
emptylist = []
print("Dave" in users)

print(users[0])
print(users[-2])
print(users.index("Sara"))
print(users[0:2])
print(users[0:])
print(users[:-1])
print(len(data))

users.append("Lavesh")
print(users[0:])

users += ["Saket"]
users.extend(["Ayush", "Yash"])
print(users[0:])

users.extend(data)
print(users)

users.insert(0, "Bob")
print(users)
users[3:3] = ["Yashpreet", "Nitesh"]
print(users)
users[1:3] = ["Robert", "JPJ"]
print(users)

users.remove("Bob")
print(users)
print(users.pop())
print(users)
del users[0]
print(users)
# del data
data.clear()
print(data)
users.pop()

# Sorting
users[1:2] = ["babita"]
users.sort(key=str.lower)
print(users)


nums = [4, 35, 15, 22, 91]
nums.reverse()
print(nums)
""" nums.sort(reverse=True)  # Printing in Descending order
print(nums) """

print(sorted(nums, reverse=True))  # reverse without losing the original list
print(nums)

numscopy = nums.copy()
mycopy = nums[:]
mynums = nums[:]
print(numscopy)
mycopy.sort()
print(mycopy)  # list is permanently changed
print(mynums)
print(type(nums))
mylist = list[1, "Neil", True]
print(mylist)

# Tuples--they cannot be changed.

mytuple = tuple(("Lavesh", 19, True))
anothertuple = (1, 2, 4, 8, 2, 2)
print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# How to append a tuple by creating another tuple.
newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
# No duplicates are allowed in Sets
nums = {1, 2, 2, 3, 4}
print(nums)
