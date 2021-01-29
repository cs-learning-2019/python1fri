# Focus Learning: Python Level 1
# Animations
# Kavan Lam
# Jan 22, 2020

# Contents
# 1) Simple animation of a ball moving to the right
# 2) Animation of a ball moving up and down (bouncing off walls)
# 3) Same as 2 but with a square
# 4) Be able to switch the direction of animation with mouse pressed
# 5) Keep track of number of bounces and display on the screen


# Section 1
"""
x = 100
y = 100

def setup():
    size(900, 900)
    
def draw():
    global x
    global y
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Draw the circle (ball)
    ellipse(x, y, 50, 50)
    
    # Move the circle (ball)
    x = x + 5
"""

# Section 2
"""
x = 450
y = 450
direction = 1  # 1 = go down   -1 = go up

def setup():
    size(900, 900)
    
def draw():
    global x
    global y
    global direction
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Draw the circle (ball)
    ellipse(x, y, 50, 50)
    
    # Move the circle (ball)
    y = y + (direction * 5)
    
    # Check for hitting the top or bottom wall
    if y >= 900:
        direction = -1
    elif y <= 0:
        direction = 1
"""

# Section 3
"""
x = 450
y = 450
direction = 1  # 1 = go down   -1 = go up

def setup():
    size(900, 900)
    
def draw():
    global x
    global y
    global direction
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Draw the rectangle
    rect(x, y, 50, 50)
    
    # Move the rectangle
    y = y + (direction * 3)
    
    # Check for hitting the top or bottom wall
    if y >= 850:
        direction = -1
    elif y <= 0:
        direction = 1
"""

# Section 4
"""
x = 450
y = 450
direction = 1  # 1 = go down or go right    -1 = go up or go left
direction_of_animation = "Vertical"  # this variable is either Vertical or Horizontal

def setup():
    size(900, 900)
    
def draw():
    global x
    global y
    global direction
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Draw the circle (ball)
    ellipse(x, y, 50, 50)
    
    # Move the circle (ball)
    if direction_of_animation == "Vertical":
        y = y + (direction * 5)
    elif direction_of_animation == "Horizontal":
        x = x + (direction * 5)
    
    # Check for hitting the top or bottom wall
    if y >= 900:
        direction = -1
    elif y <= 0:
        direction = 1
        
    if x >= 900:
        direction = -1
    elif x <= 0:
        direction = 1

def mousePressed():
    global direction_of_animation
    print("Mouse is pressed you need to swap the direction of animation")
    if direction_of_animation == "Vertical":
        direction_of_animation = "Horizontal"
    elif direction_of_animation == "Horizontal":
        direction_of_animation = "Vertical"
"""

# Section 5
x = 450
y = 450
direction = 1  # 1 = go down   -1 = go up
num_bounces = 0 # This will keep track of the number of bounces. It starts at zero.

def setup():
    global my_font
    size(900, 900)
    my_font = loadFont("BerlinSansFB-Bold-48.vlw")
    
def draw():
    global x
    global y
    global direction
    global num_bounces
    global my_font
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Draw the circle (ball)
    ellipse(x, y, 50, 50)
    
    # Move the circle (ball)
    y = y + (direction * 5)
    
    # Check for hitting the top or bottom wall
    if y >= 900:
        direction = -1
        num_bounces = num_bounces + 1
    elif y <= 0:
        direction = 1
        num_bounces = num_bounces + 1
        
    # Display the number of bounces
    pushStyle()
    textFont(my_font, 40)
    fill(255, 0, 0)
    text("Number of bounces: " + str(num_bounces), 100, 100)
    popStyle()
    
