from turtle import *
from random import randint

speed(0)
def wander():
    while True:
        fd(3)
        # forward 3 pixels
        if xcor() >= 200 or xcor() <= -200 or ycor() <= -200 or ycor() >= 200:
            # if the x coordinate is smaller than or equal to 200
            # or the x coordinate is bigger than or equal to -200
            # or the y coordinate is bigger than or equal to -200
            # or the y coordinate is smaller than or equal to 200
            lt(randint(90, 180))
            # turn left randomly between 90 and 180 degrees

wander()