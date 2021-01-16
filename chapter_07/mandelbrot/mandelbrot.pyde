from math import sqrt

xmin = 2.0
xmax = -2.0

ymin = 2.0
ymax = -2.0

rangex = xmax - xmin
rangey = ymax - ymin


def setup():
    global xscl, yscl
    size(600, 600)
    colorMode(HSB)
    noStroke()
    xscl = float(rangex) / width
    yscl = float(rangey) / height


def draw():
    for x in range(width):
        for y in range(height):
            z = [(xmin + x * xscl), (ymin + y * yscl)]
            c = [-0.8, 0.156]
            col = julia(z, c, 100)
            if col == 100:
                fill(0)
            else:
                fill(3 * col, 255, 255)
            rect(x, y, 1, 1)
            
            

def julia(z, c, num):
    count = 0
    z1 = z
    while count <= num:
        if magnitude(z1) > 2.0:
            return count
        z1 = cAdd(cMult(z1, z1), c)
        count += 1
    return num

def mandelbrot(z, num):
    count = 0
    z1 = z
    while count <= num:
        if magnitude(z1) > 2.0:
            return count
        z1 = cAdd(cMult(z1, z1), z)
        count += 1
    return num


def cAdd(a, b):
    return [a[0] + b[0], a[1] + b[1]]


def cMult(u, v):
    return [u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0]]


def magnitude(z):
    return sqrt(z[0] ** 2 + z[1] ** 2)
