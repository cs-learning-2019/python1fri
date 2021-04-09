# Focus Learning: Python Level 1
# Text, Images and Sounds in Processing
# Kavan Lam
# Oct 16, 2020

# You can get sound effects free from here http://soundbible.com/
# Tell Processing we want to uses the minim library
add_library("minim")

def setup():
    global font1
    global dog
    global mario
    
    size(900, 700)
    
    # Here we load a picture. The pictures should be in .jpg or .png format.
    # Also do not forget to go to sketch >> Add file first
    dog = loadImage("dog.jpg")
    mario = loadImage("mario.jpg")
    
    # Load in a font
    font1 = loadFont("BodoniMTCondensed-BoldItalic-48.vlw")
    
    minim = Minim(this)  # store a cd player in to the minim variable
    monkey_sound = minim.loadFile("monkey.mp3")
    
    # .loop will replay the sound when it is finished
    # .play will only play the sound from start to finish one time
    monkey_sound.loop() 
    
    
def draw():
    background(0, 0, 0)
    
    # Draw a simple rectangle
    rect(100, 200, 200, 50)
    
    # Draw some text
    pushStyle()
    fill(255, 0, 0)
    textFont(font1, 50)
    text("Blah blah blah", 50, 100)
    popStyle()
    
    # Draw a picture to the screen
    pushStyle()
    image(dog, 400, 300, 400, 300)
    popStyle()
    
    # Draw a picture to the screen
    pushStyle()
    image(mario, 100, 300, 300, 200)
    popStyle()
