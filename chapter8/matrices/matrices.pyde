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
    noFill()


transformation_matrix = [[0, -1], [1, 0]]


def draw():
    global xscl, yscl
    background(255)
    translate(width / 2, height / 2)
    grid(xscl, yscl)
    
    rot = map(mouseX, 0, width, 0, TWO_PI)
    tilt = map(mouseY, 0, height, 0, TWO_PI)
    newmatrix = transpose(multMatrics(rottilt(rot, tilt), transpose(fmatrix)))
    strokeWeight(2)
    stroke(255, 0 , 0)
    graphPoints(newmatrix, edges)
    

def grid(xscl, yscl):    
    strokeWeight(1)
    stroke(0, 255, 255)
    for i in range(xmin, xmax + 1):
        line(i * xscl, ymin * yscl, i * xscl, ymax * yscl)
    for i in range(ymin, ymax + 1):
        line(xmin * xscl, i * yscl, xmax * xscl, i * yscl)
    stroke(0)
    line(0, ymin * yscl, 0, ymax * yscl)
    line(xmin * xscl, 0, xmax * xscl, 0)


#fmatrix = [[0, 0], [1, 0], [1, 2], [2, 2], [2, 3], [1, 3], [1, 4], [3, 4], [3, 5], [0, 5]]
fmatrix = [
            [0, 0, 0], [1, 0, 0], [1, 2, 0], [2, 2, 0], [2, 3, 0],
            [1, 3, 0], [1, 4, 0], [3, 4, 0], [3, 5, 0], [0, 5, 0],
            [0, 0, 1], [1, 0, 1], [1, 2, 1], [2, 2, 1], [2, 3, 1],
            [1, 3, 1], [1, 4, 1], [3, 4, 1], [3, 5, 1], [0, 5, 1],
          ]
edges =   [
            [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8],
            [8, 9], [9, 0], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15],
            [15, 16], [16, 17], [17, 18], [18, 19], [19, 10], [0, 10], [1, 11],
            [2, 12], [3, 13], [4, 14], [5, 15], [6, 16], [7, 17], [8, 18], [9, 19],
          ]
'''
def graphPoints(matrix):
    beginShape()
    for pt in matrix:
        vertex(pt[0] * xscl, pt[1] * yscl)
    endShape(CLOSE)
'''

def graphPoints(pointList, edge):
    for e in edges:
        line(pointList[e[0]][0] * xscl, pointList[e[0]][1] * yscl, 
             pointList[e[1]][0] * xscl, pointList[e[1]][1] * yscl)


def rottilt(rot, tilt):
    rotmatrix_y = [[cos(rot), 0.0, sin(rot)],
                   [0.0, 1.0, 0.0],
                   [-sin(rot), 0.0, cos(rot)]
                  ]
    rotmatrix_x = [[1.0, 0.0, 0.0],
                   [0.0, cos(tilt), sin(tilt)],
                   [0.0, -sin(tilt), cos(tilt)]
                  ]
    return multMatrics(rotmatrix_y, rotmatrix_x)

def addMatrices(a, b):
    c = [
        [a[0][0] + b[0][0], a[0][1] + b[0][1]],
        [a[1][0] + b[1][0], a[1][1] + b[1][1]]
    ]
    return c


def multMatrics(a, b):
    m = len(a)
    n = len(b[0])
    newmatrix = []
    for i in range(m):
        row = []
        for j in range(n):
            sum1 = 0
            for k in range(len(b)):
                sum1 += a[i][k] * b[k][j]
            row.append(sum1)
        newmatrix.append(row)
    return newmatrix


def transpose(a):
    output = []
    m = len(a)
    n = len(a[0])
    for i in range(n):
        output.append([])
        for j in range(m):
            output[i].append(a[j][i])
    return output


a = [[1, 2, -3, -1]]
print(transpose(a))
