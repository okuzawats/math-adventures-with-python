xmin = -10
xmax = 10

ymin = -10
ymax = 10

rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600, 600)
    xscl = width / rangex
    yscl = -height / rangey


def draw():
    global xscl, yscl
    background(255)
    translate(width / 2, height / 2)
    grid(xscl, yscl)
    graphFunction()
    


def grid(xscl, yscl):    
    strokeWeight(1)
    stroke(2, 255, 255)
    for i in range(xmin, xmax + 1):
        line(i * xscl, ymin * yscl, i * xscl, ymax * yscl)
    for i in range(ymin, ymax + 1):
        line(xmin * xscl, i * yscl, xmax * xscl, i * yscl)
    stroke(0)
    line(0, ymin * yscl, 0, ymax * yscl)
    line(xmin * xscl, 0, xmax * xscl, 0)


def f(x):
    return x ** 2


def graphFunction():
    x = xmin
    while x <= xmax:
        fill(0)
        line(x * xscl, f(x) * yscl, (x + 0.1) * xscl, f(x + 0.1) * yscl)
        x += 0.1
