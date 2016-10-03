import random
    
velocidade = 0
y = 0
x1 = 0
x2 = 0
def setup():
    size(500, 500)
    background(100)
    frameRate(60)
    
def draw():
    global y 
    y = random.randint(0, width)
    global x1 
    x1 = random.randint(1, height)
    global x2
    x2 = random.randint(1, height)
    line(y, x1, y, x2)