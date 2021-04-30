def setup():
    size(900, 900)

def draw():
    background(0, 0, 0)
    
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
