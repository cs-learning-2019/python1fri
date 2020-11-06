# Focus Learning: Python 1 
# If statements part 1
# Kavan Lam
# Nov 6, 2020


# Skill 1
# Ex 1
# if (condition):  (you can think of the : as saying then)
#   do something
if 30 < 5:
    print("Pikachu!")

print("Hello") # There is no tab so this line is not part of the if statement

# Ex 2
print("-----------------------------------")
# single equal sign is for taking something and putting it into a variable
# Double equal sign is for comparing the thing on the right and left and seeing if they are the same
amt = 25
if amt == 20:
    print("$20")
else:  # else is an extension to the if statement and takes care of what to do if everything else fails
    print("You do not have 20 bucks")
    
# Challenges
# A
print("-----------------------------------")
age = 30
if age > 12:
    print("Ha ha a joke")
else:
    print("You not old enough. No joke for u.")


# Skill 2
print("----------------------------------")
# Python will use only the first case that works in a single if statement
mark = 85
if mark > 90:
    print("A+")
elif mark > 80:
    print("A")
elif mark > 70:
    print("B")
elif mark > 60:
    print("C")
elif mark > 50:
    print("D")
else:
    print("Needs help.")
# Above is one if statement
# Note: we do not give a condition for else since it should take care of what happens if non
# of the cases above worked

# Practice Question 1
print("------------------------------------------")
a = 20
# Below is actually 2 if statements which are independent of each other
if a > 17:
    print("You're an adult")
if a > 13:
    print("You're a teenager")
else:
    print("You're a kid.") 

print("------------------------------------")
# This is one if statement
if a > 17:
    print("You're an adult")
elif a < 13:
    print("You're a teenager")
else:
    print("You're a kid.")

# Practice Question 2
print("-------------------------")
peanut_sales = 200
if peanut_sales < 200:
    print("You have not sold enough peanuts.")
else:
    print("Quota reached.")
   
print("-------------------------")
month = 12
if month < 3:
    print("Winter")
elif month < 6:
    print("Spring")
elif month < 9:
    print("Summer")
else:
    print("Fall")
