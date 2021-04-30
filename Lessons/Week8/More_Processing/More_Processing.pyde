# Focus Learning: Python Level 1
# More Processing
# Kavan Lam
# March 26, 2021

add_library("minim")

def setup():
    global font1
    global sound1
    
    size(900, 900)
    font1 = loadFont("Harrington-48.vlw")  # it is loading it from the data folder
    
    my_sound_player = Minim(this)
    sound1 = my_sound_player.loadFile("monkey.mp3")
    #my_sound_player.loadFile("monkey.mp3").loop()


def draw():
    global font1
    global sound1
    
    background(0, 0, 0)
    fill(255, 0, 0)
    textAlign(CENTER)
    textFont(font1, 100)
    #textSize(100)
    text("Hello World", 450, 450)
    
    #sound1.loop() this is no good
    sound1.setGain(-30)  # set the volume
    
    sound1.play()  # This is ok
    
    
    
