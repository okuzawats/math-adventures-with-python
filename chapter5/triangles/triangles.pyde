def setup():
    size(600, 600)
    rectMode(CENTER)


t = 0


def draw():
    global t
    background(255)
    translate(width/2, height/2)
    for i in range(90):    
        rotate(radians(360 / 90))
        pushMatrix()
        translate(200, 0)
        rotate(radians(t + 1 * 360 / 90))
        tri(100)
        popMatrix()
    t += 0.5


def tri(length):
    noFill()
    triangle(0, -length, -length * sqrt(3) / 2, length / 2, length * sqrt(3) / 2, length / 2)
