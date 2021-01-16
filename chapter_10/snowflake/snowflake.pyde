def setup():
    size(600, 600)


def draw():
    background(255)
    translate(100, 200)
    level = int(map(mouseX, 0, width, 0, 7))
    snowflake(400, level)


def snowflake(sz, level):
    for i in range(3):
        segments(sz, level)
        rotate(radians(120))


def segments(sz, level):
    if level == 0:
        line(0, 0, sz, 0)
        translate(sz, 0)
    else:
        segments(sz / 3.0, level - 1)
        rotate(radians(-60))
        segments(sz / 3.0, level - 1)
        rotate(radians(120))
        segments(sz / 3.0, level - 1)
        rotate(radians(-60))
        segments(sz / 3.0, level - 1)
