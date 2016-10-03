import random
velocidadex = 2.0
velocidadey = 2.0
direcaox = 1
direcaoy = 1
raio = 60
x = 60
y = 60
gravidade = 9.8

def setup():
    size(500, 600)
    frameRate(60)
    background(0)

def draw():
    background(102)
    fill(255, 255, 255)
    text("OI ROMULO", 10.0, 10.0)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    fill(r, g,b)
    stroke(0, 20, 120)
    ellipse(x, y, raio, raio)
    global x
    global velocidadex
    x = x + (velocidadex*direcaox)
    global y
    global direcaoy
    global velocidadey
    global gravidade
    y = y + (direcaoy*velocidadey)
    velocidadey = velocidadey + gravidade*direcaoy/60
    if(x > width-raio/2 or x < raio/2):
        velocidadex = velocidadex * -1
    if(y > height-raio/2 or y < raio/2):
        direcaoy = direcaoy * -1
        
def mouseClicked():
    global direcaoy
    direcaoy = direcaoy * -1