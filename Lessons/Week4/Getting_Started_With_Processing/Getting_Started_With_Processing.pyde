# Focus Learning: Python Level 1
# Getting started with Processing
# Kavan Lam
# Oct 9, 2020


# def = defining
# Note all of the code inside a section must be tabbed (4 spaces)
def setup():
    # Note x is always first   so size(x, y)   x is left to right and y is top to bottom
    size(1100, 600)
    
def draw():
    # RGB value is used to pick what color you want
    # Each number needs to be 0-255
    # White ---> (255, 255, 255)
    # Black ---> (0, 0, 0)
    # Yellow --> (255, 255, 0)
    background(255, 200, 0)  
    
    # Draw a rectangle
    pushStyle() # Start the styling
    fill(255, 0, 0)  # Fill in the shape with some color
    stroke(0, 0, 255) # Fill in the perimeter of the shape with some color
    strokeWeight(5)
    rect(0, 200, 50, 50) # rect(x, y, length, width) to be clear the x, y is the top left corner of the rect
    popStyle()  # End the styling
    
    
    # Draw a rectangle
    pushStyle()
    fill(0, 255, 0)  # Fill in the shape with some color
    stroke(0, 0, 255) # Fill in the perimeter of the shape with some color
    rect(100, 300, 50, 50)
    popStyle()
    
    # Draw some text
    pushStyle()
    fill(0, 255, 255)
    textSize(50)
    text("Hello World", 400, 50)
    popStyle()
    
    # Draw a circle/oval
    pushStyle()
    fill(0, 255, 255) # Use this to change the color of the inside of the shape
    stroke(255, 0, 255) # Use this to change the color of the perimeter of the shape
    ellipse(450, 300, 100, 100)  # ellipse(x, y, length, width)
    popStyle()
    
    # Draw a line
    pushStyle()
    fill(255, 0, 0) # Fill does not work on lines since a line is not a shape. Fill only works on shapes.
    stroke(255, 0, 0) # You need to use stroke to change the color of a line
    strokeWeight(5)
    line(100, 200, 300, 400)  # line(x, y, x, y)  The first two is for the starting point. The last 2 is for the ending point.
    popStyle()
