# Focus Learning Python Level 1
# Intro to Python
# Sept 25, 2020
# Kavan Lam


### Skill 1 ###
# A comment is just extra notes for the human reader. Comments are not real code and is ignored by Python
# print is a function that takes what you type and puts it into the output (black section at the bottom)
print("Welcome to Python")
print("What are \n these hacks?")  # \n --> is a special character and it makes a new line
# print("What are \nthese hacks?") 
print("\t What is going on? :)") # \t is a tab = 4 spaces
print("SPAM" * 20)  # * = multiplication

# Challenges
# A
print("Baseball")

# B
print("*" * 9)  # The first row
print("*       *")
print("*       *")
print("*       *")
print("*       *")
print("*       *")
print("*" * 9)  # The last row


### Skill 2 ###
print("-------------------------------------------")
# A String is anything inside " " (quotes)   Eg / "hi"  is a string

print("Hello" + " What is this?") # "Hello" + " What is this?" = "Hello What is this?"

# Above is an example of String Concatenation 
# Concatenation is a fancy word for addition

print("\t"*2 + "-.-.- " * 5 + "}} }")

# Practice Question
# 3/4
print("You're amazing!" + " And the best!" + " And better than all the rest!")



### Skill 3 ###
print("-----------------------------------------")
# A variable is a helping hand that is able to hold on to some piece of data
# In python we have lot of different types of data
# 1) Strings   eg/ "Hello"
# 2) int       eg/ 10, 20, -10, 0
# 3) boolean   eg/ True, False
# 4) float     eg/ 54.6, 10.0, 1.1, -100.678
bugs = 10
colour = "Red"
like_cheese = False
fav_num = 54.3
dogs = "I like dogs"

# Rules for naming variables
# 1) Does not start with a number. You need to start it with a letter.
# 2) No spaces. Instead use underscores.
# 3) Only letters, numbers and _

print(bugs)
print("My favourite colour is " + colour)
print(like_cheese)
print(fav_num*10)
print(dogs)

# Challenges
# B
shoe_sz = 8
#print("My shoe size is " + shoe_sz)  # it does not make sense to ask someone to add 5 apples with 2 pears
print("My shoe size is " + str(shoe_sz)) #  str(8) ---> "8"

# C
age = 30
print("You need to wait " + str(100 - age))

# Practice
# 2
"""
We use the str() function to convert a number into a string

BTW this is what we call a multiline comment
"""
