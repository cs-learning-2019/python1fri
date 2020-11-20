# Focus Learning: Python Level 1
# For loops
# Nov 20, 2020
# Kavan Lam

# If we wanted to print the numbers from 0 to 5
print(0)
print(1)
print(2)
print(3)
print(4)
print(5)

# What if we wanted to print the numbers from 0 to 100
# This is not going to be fun... is there an easier method

# Ex 1 
print("--------------------------------------")
# for (variable) in (something):
for i in range(10):   # range will give you back a range of numbers. Python will always go one less than what you said.
    print(i)
    
    
print("Hello")  # This line is not part of the for loop since it is not tabbed

# Ex 2
print("---------------------------------------")
for j in range(8):
    print("&"*j)
    
    
# Ex 3
print("---------------------------------------")
for q in range(2, 7):
    print(str(q) + " bugs")


# Ex 4
print("---------------------------------------")
for p in range(4, 10, 2):  # 4 is the start, 10 is the end and 2 is the amount we should count by
    print(p * 7)


# Ex 5
print("---------------------------------------")
for t in range(10, 0, -1):
    print(t)
    
print("Blastoff!")


# Ex 6
print("---------------------------------------")
for character in "bugaboo":
    print(character)


# Ex 7 
print("-----------------------------------------")
size = 80
print("-" * size)

for row in range(size - 2):
    print("|" + " " * (size - 2) + "|")

print("-" * size)
