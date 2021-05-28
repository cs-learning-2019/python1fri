# Focus Learning: Python Level 1
# If statements part 2
# Kavan Lam
# May 28, 2021

# Skill 1: AND Operator  --> and is one of the logical operators
wantCheese = True  # This is a boolean (there is only True and False)
wantBacon = True
if wantCheese == True and wantBacon == True:
    print("Bacon Cheese Burger")
elif wantCheese == True and wantBacon == False:
    print("Cheese Burger")
elif wantCheese == False and wantBacon == True:
    print("Bacon Burger")
    
#Skill 2: OR operator
print("----------------------------------------------------------------")
wantCream = True
wantSugar = False
if wantCream == True or wantSugar == True:
    print("Offer cream, offer sugar")
else:
    print("Don't offer either")
    

#Skill 3: not operator
fiction = True
if not(fiction == True):
    print("This is a true story")
else:
    print("This is a made up story")

    
    
    
    
    
    
