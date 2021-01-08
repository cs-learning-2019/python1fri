# Focus Learning: Python Level 1
# User interaction using the keyboard and mouse 
# Kavan Lam
# Jan 8, 2021

# Contents
# 1) How to get keyboard input using key 
# 2) How to get mouse input (the position of the mouse)
# 3) How to move an object using the mouse (object follows the mouse)
# 4) How to move an object using WASD or the arrow keys (using keyCode)

# Section 1
"""
def setup():
    size(900, 900)

def draw():
    rect(100, 100, 50, 50)
    
def keyPressed():
    if key == "W" or key == "w":
        print("You pressed W")
    elif key == "A" or key == "a":
        print("You pressed A")
    elif key == "S" or key == "s":
        print("You pressed S")
    elif key == "D" or key == "d":
        print("You pressed D")
"""

# Section 2
"""
def setup():
    size(900, 900)

def draw():
    rect(100, 100, 50, 50)

def mousePressed():
    print("You click the mouse")
    print(mouseX, mouseY)
"""

# Section 3
"""
def setup():
    size(900, 900)

def draw():
    # clear the previous frame/circle
    background(0, 0, 0)
    
    # Draw the new circle
    ellipse(mouseX, mouseY, 50, 50)
"""

# Section 4
x = 100
y = 100

def setup():
    size(900, 900)

def draw():
    global x
    global y
    
    # clear the previous frame
    background(0, 0, 0)
    
    # Draw the new stuff
    rect(x, y, 50, 50)
    
def keyPressed():
    global x
    global y
    
    if keyCode == UP:
        y = y - 10
    elif keyCode == LEFT:
        x = x - 10
    elif keyCode == DOWN:
        y = y + 10
    elif keyCode == RIGHT:
        x = x + 10

        

    
