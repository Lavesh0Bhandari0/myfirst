# Dictionaries
band = {"vocals": "plant", "guitar": "page"}
band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# list all the keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify a key exists
print("guitar" in band)
print("triangle" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)
print(band.popitem())  # Will print a tuple

# Delete and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2


# Copy dictionaries

""" band2 = band  # Creates a reference and not a copy.
print("Bad copy!")
print(band2)
print(band)
band2["drums"] = "Lavesh"
print(band)
 """

band2 = band.copy()
band2["drums"] = "Lavesh"
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)


# Nested Dictionary
member1 = {"name": "plant", "instrument": "tabla"}
member2 = {"name": "pot", "instrument": "flute"}

band = {"member1": member1, "member2": member2}
print(band)
print(band["member1"]["name"])

# Sets

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicates are allowed in Sets
nums = {1, 2, 2, 3, 4}
print(nums)

# True value is a dupe of 1, False is a dupe of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# Check if a value is in a set.
print(2 in nums)

# but you cannot refer to an element in the set with an index position or a key

# Add a new element to a set
nums.add(8)
print(nums)

# Add elemets from one set to another
morenums = {5, 6, 7, 8}
nums.update(morenums)
print(nums)
# You can use update with list, tuples and dictionaries, too.

# Merge two set to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

newset = one.union(two)
print(newset)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3}

one.intersection_update(two)
print(one)


# Keep everthing except duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
