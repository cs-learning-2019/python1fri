def setup():
    size(900, 900)
    background(0, 0, 0)

def draw():
    pushStyle()
    stroke(255, 0, 0)  # use red for the point
    strokeWeight(15)
    point(100, 100)
    point(300, 100)
    popStyle()
    
    pushStyle()
    stroke(0, 255, 0)
    strokeWeight(5)
    line(100, 100, 300, 100)
    popStyle()


x = 0
y = 0
def mousePressed():
    global x
    global y
    x = mouseX
    y = mouseY

def mouseReleased():
    stroke(255, 255, 0)
    strokeWeight(5)
    line(x, y, mouseX, mouseY)
