from turtle import *
shape('turtle')
speed(1)
# speed 0 is the fastest, speed 1 the slowest

def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)

square(50)
