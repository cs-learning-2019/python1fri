# Foucs Learning: Python Level 1
# More Loops with list
# Dec 18, 2020
# Kavan Lam

# Ex 1
print("------------------------------------------")
for counter in range(0, 6):
    print(counter)
    
    
# Ex 2
print("------------------------------------------")
counter = 0
while counter < 6:
    print(counter)
    counter = counter + 1
   
     
# Ex 3
print("------------------------------------------")
myList = [15, 12, 3, 7]
for item in myList:
    print(item)


# Ex 4
print("------------------------------------------")
myList = [15, 12, 3, 7]
counter = 0
while counter < len(myList):
    print(myList[counter])
    counter += 1   # Same as counter = counter + 1


# Ex 5
print("------------------------------------------")
myList = [15, 12, 3, 7]
for counter in range(len(myList)):
    print(myList[counter])


# Ex 6
print("------------------------------------------")
myList = [15, 12, 3, 7]
counter = 0
while counter < len(myList):
    print(myList[counter])
    counter += 1  # counter = counter + 1

# Ex 7
print("------------------------------------------")
food = "peanut butter"  # Spaces are considered as valid characters
for letter in food:
    print(letter)


# Ex 8
print("------------------------------------------")
food = "peanut butter"  # Length is 13  (Note: The space is at index 6)
index = 0
while index < len(food):
    print(food[index])
    index += 1
 
 
# Ex 9
print("------------------------------------------") 
greeting = "Hello earthlings!"  # Length is 17 . The last index is 16
for index in range(len(greeting)-1, -1, -1):
    print(greeting[index])
 
 
# Ex 10
print("------------------------------------------") 
greeting = "Hello earthlings!"
index = len(greeting) - 1
while index >= 0:
    print(greeting[index])
    index = index - 1
    
    
# Ex 11
print("------------------------------------------") 
toReverse = "Coding rocks!"
for index in range(len(toReverse)-1, -1, -1):
    print(toReverse[index])
 
 
# Ex 12
print("------------------------------------------") 
toReverse = "Coding rocks!"
index = len(toReverse)-1
while index >= 0:
    print(toReverse[index])
    index -= 1


"""
+= 3  --> just means take your variable and increase it's value by three
a = 10
a += 3  --> This will make a = 13  (same as doing a = a + 3)

-=  it is the same thing as += but now you subtract
a = 10
a -= 3  --> This will make a = 7  (same as doing a = a - 3)
"""
