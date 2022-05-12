from turtle import *
shape('turtle')
speed(3)
# speed 0 is the fastest, speed 1 the slowest

def square():
    for i in range(4):
        forward(100)
        right(90)

square()
