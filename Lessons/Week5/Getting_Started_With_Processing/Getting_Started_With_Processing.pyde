# Focus Learning: Python Level 1
# Getting started with Processing
# Kavan Lam
# March 5, 2021

def setup():
    print("Setting up my project")
    size(700, 700)


def draw():
    fill(255, 255, 0)
    rect(0, 200, 50, 50)  # rect = rectangle  eg/ rect(x, y, length, width)  and x, y is the top left corner of the rect
    rect(350, 350, 150, 50)
    






























### IGNORE THIS ####
"""
# def = defining
# Note all of the code inside a section must be tabbed (4 spaces)
def setup():
    # Note x is always first   so size(x, y)   x is left to right and y is top to bottom
    size(900, 600)
    
def draw():
    background(255, 255, 0) # We use RGB colors. Each number is from 0-255
    # White ---> (255, 255, 255)
    # Black ---> (0, 0, 0)
    
    pushStyle()
    fill(255, 0, 0) # Use this to change the color of the inside of the shape
    stroke(0, 0, 255) # Use this to change the color of the perimeter of the shape
    strokeWeight(4)  # Use this to change the thickness of the perimeter of the shape
    rect(0, 200, 50, 50)  # rect = rectangle  eg/ rect(x, y, length, width)  and x, y is the top left corner of the rect
    popStyle()
    
    pushStyle()
    fill(0, 255, 255) # Use this to change the color of the inside of the shape
    stroke(255, 0, 255) # Use this to change the color of the perimeter of the shape
    rect(200, 300, 100, 50)
    ellipse(450, 300, 100, 100)  # ellipse(x, y, length, width)
    popStyle()
    
    pushStyle()
    stroke(255, 0, 0)
    strokeWeight(4)
    line(100, 100, 400, 400)   # line(x, y, x, y)  The first two is for the starting point. The last 2 is for the ending point.
    popStyle()
    
    pushStyle()
    fill(20, 178, 102)
    textSize(50)
    text("Hello World", 300, 50)  # text("What you want to say", x, y) 
    popStyle()
"""
