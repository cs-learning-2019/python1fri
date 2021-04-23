add_library("minim")

def setup():
    global myImg
    size(900, 900)
    myImg = loadImage("water.jpg")
    
    music_player = Minim(this)
    bell_sound = music_player.loadFile("bell.wav")
    
    bell_sound.play()

def draw():
    global myImg
    
    background(0, 0, 0)
    image(myImg, 650, 100, 200, 200)
    
    
