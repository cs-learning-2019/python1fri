# Focus Learning: Python Level 1
# If statements part 2
# Kavan Lam
# Nov 13, 2020

# Skill 1: AND operator
wantCheese = True
wantBacon = True
if wantCheese == True and wantBacon == True:
    print("Bacon Cheese Burger")
elif wantCheese == True and wantBacon == False:
    print("Cheese Burger")
elif wantCheese == False and wantBacon == True:
    print("Bacon Burger")
else:
    print("Burger")
    
# and is a logical operator. And is very strict. Each piece of And needs to be true
# in order for the condition to be true.

# Challenge A
# Done (look above)

# Challenge B
# Truth table for the AND logical operator
"""
A    B    A and B
T    T    T
T    F    F
F    T    F
F    F    F
"""


# Skill 2: OR operator
print("--------------------------------------------")
wantCream = False
wantSugar = True
if wantCream == True or wantSugar == True:
    print("Offer cream or offer sugar")
else:
    print("Don't offer either")

# OR is less strict. As long as one thing is good then the whole thing is good.

# Challenge C
# Truth table for the OR logical operator
"""
A    B    A OR B
T    T    T
T    F    T
F    T    T
F    F    F
"""


# Skill 3: NOT operator
print("----------------------------------------")
fiction = True
if not fiction == True:
    print("This is a true story")
else:
    print("This is a made up story")

# Challenge D
# Truth table for the NOT logical operator
"""
A   NOT A
T   F
T   F
F   T
F   T
"""
