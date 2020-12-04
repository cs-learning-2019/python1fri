# Focus Learning: Python Level 1
# Python Lists
# Kavan Lam
# Dec 4, 2020

# With three students we can do this
age1 = 10
age2 = 12
age3 = 11

# But what if we had 1000 students (oh no!!!)
# We need 1000 variables
# Is there an easier way to keep track of all the ages in the class?
# YES, we can use Python List

ages = [10, 12, 11, 9, 8, 12, 10]  # This is a python List
print(ages[0])
print(ages[3])

# Now lets actually look at the worksheet
print("-------------------------------")
pets = [3, 5, 1, 9, 0, 2]
print(pets[0])
print(pets[3])
print(pets)

# We can change the numbers in the list
pets[2] = 6
pets[5] = pets[5] + 3
print(pets)

# This can tell you how many numbers we have in a list   len = length
print(len(pets))

# There is no such thing as index 8
# print(pets[8])  this code will not work
print("----------------------------------")
print(pets[-1]) # Negative just goes in reverse



# Adding to and Deleting From Lists
print("-------------------------------------")
names = ["john", "kim", "boo", "yo"]
names.append("kavan")  # Adding a new name to the list
names[3] = "yoo"
print(names)

names.pop(1) # Removing a name from the list
print(names)
