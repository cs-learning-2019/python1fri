def setup():
    size(900,  600)
    
def draw():
    background(0, 0, 0)
    
    pushStyle()
    stroke(255, 0, 0)
    strokeWeight(15)
    point(200, 100)
    popStyle()
    
    pushStyle()
    stroke(255, 255, 0)
    strokeWeight(15)
    point(200, 150)
    popStyle()
