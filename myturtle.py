from turtle import *


def square(side_length=100):
    for i in range(4):
        forward(side_length)
        right(90)


def triangle(side_length=100):
    for i in range(3):
        forward(side_length)
        right(120)


def polygon(sides):
    for i in range(sides):
        forward(100)
        right(360 / sides)


shape('turtle')
speed(0)

# assignment1-5
for i in range(60):
    square(i * 5)
    right(5)

# not to finish script automatically
input = input('input something here')
