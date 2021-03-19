# Focus Learning: Python 1 Fri
# Getting started with Processing Homework
# Kavan Lam
# March 19, 2021

# Question 1
# The dot will appear in the bottom right corner for (600, 900)
# The dot will appear in the top left corner for (100, 150)

# Question 2
# The first two numbers are for the location of the rectangle (top-left corner of the rectangle)
# The last two numbers are for the size, it is the length and then the width

# Question 3
# The first two numbers are for the location of the circle
# The last two numbers are for the length and width of the circle

# Question 4
def setup():
    size(800, 300)
    background(0, 0, 0)
    
def draw():
    # Draw the text
    textAlign(CENTER)
    textSize(30)
    fill(0, 210, 0)
    text("Hello world", 400, 50)
    
    # Draw the circles
    fill(0, 0,  255)
    ellipse(400, 120, 85, 85)
    fill(255, 255,  255)
    ellipse(400, 160, 85, 85)
    fill(255, 0,  0)
    ellipse(400, 200, 85, 85)
    
    # Draw the lines
    pushStyle()
    stroke(0, 255, 0)
    line(100, 100, 300, 250)
    popStyle()
    pushStyle()
    stroke(255, 0, 0)
    line(500, 250, 700, 100)
    popStyle()
    
    # Draw the rectangles
    rect(30, 85, 40, 170)
    fill(255, 255,  0)
    rect(720, 85, 40, 170)
    
    
    
    
    
