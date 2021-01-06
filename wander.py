from turtle import *
from random import randint


def wander():
    while True:
        fd(3)
        if xcor() >= 200 or xcor() <= -100 or ycor() <= -100 or ycor() >= 200:
            lt(randint(90, 100))


speed(0)
wander()
