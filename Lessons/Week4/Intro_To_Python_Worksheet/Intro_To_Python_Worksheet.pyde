# Focus Learning Python Level 1
# Intro to Python
# Feb 26, 2021
# Kavan Lam


##### SKILL 1 #####
# This is a comment and not actual code
print("Welcome to Python!")

# Backslahes \\\\\
# \n is something special --> It means newline
print("------------------------------------------")
print("What are \n these hacks?")

# \t is also special --> It means tab (4 spaces)
print("------------------------------------------")
print("\t What is going on? :)")

# 2 x 2 = 4  --> 2 * 2 = 4
print("------------------------------------------")
print("SPAM" * 5)
print((3*6)-5)

# Challenges
# A
print("------------------------------------------")
print("baseball")

# B (This is an example of ASCII ART)
print("------------------------------------------")
print("*********")
print("*       *")
print("*       *")
print("*       *")
print("*       *")
print("*********")

##### SKILL 2 #####
# Concatenation --> Fancy word for adding together
# String --> Is some text enclosed with "" quotes
# String Concatenation --> Just means adding two strings together to form a bigger string
print("------------------------------------------")
print("Hello" + "What is this?")

print("------------------------------------------")
print("Banana " * 3 + "Orange you glad I didn't say banana?")

print("------------------------------------------")
print("\t"*2 + "-.-.- " * 5 + "|||")

# Challenges
# A
print("------------------------------------------")
print("Kavan " + "Lam") # or you can do this print("Kavan" + " " + "Lam")

# B
print("------------------------------------------")
print("*********")
print("*       *")
print("* Kavan *")
print("*       *")
print("*       *")
print("*********")

# Practice Questions
# NOTE: A string in Python is just and text inbetween "" (quotation marks)
# 1) We use the + symbol to concatenate
# 2) It is useful for cases where you have text coming from different places
# and you need to combine them together. 

# 3
print("------------------------------------------")
print("You're amazing!" + " And the best! " + "And better than all the rest!")

# 4
# Without the space there would be no space between the ! and A


##### SKILL 3 (Variables) #####
# A variable is like a helping hand that can hold on to things for you. You can name the hand(s)
# whatever you like.

# The rules for naming variables
# 1) It must not start with a number. So it must begin with a letter.
# 2) It must only contain _ (underscore) , numbers or letters
# 3) No spaces in variable names

# We are creating variables
bugs = 10  # This is an example of a variable. The variable is named bugs and is holding onto 10
colour = "Red boom blah"  # This is another example of a variable. In this case it is holding onto a string
like_cheese = False  # Here the variable is named like_cheese and it is equal to False (false = 0 and true = 1)
fav_num = 54.3  # Variable name is fav_num

# We are using the variables
print("-------------------------------------------------")
print(bugs)
print("My favourite colour is " + colour)
print(like_cheese)
print(fav_num*10)

# Challenges
# B
print("-------------------------------------------------")
shoe_sz = 8
print("My shoe size is " + str(shoe_sz))
# You are not allowed to add a string with a int
