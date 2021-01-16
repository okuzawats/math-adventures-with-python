def setup():
    size(600, 600)


def draw():
    translate(width/2, height/2)
    polygon(3, 100)


def polygon(sides, sz):
    beginShape()
    for i in range(sides):
        step = radians(360 / sides)
        vertex(sz * cos(step * i), sz * sin(step * i))
    endShape(CLOSE)
    
