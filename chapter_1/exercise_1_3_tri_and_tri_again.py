from turtle import *

sidelength = 200

def triangle():
    for i in range(3):
        forward(sidelength)
        left(120)

for i in range(100):
    triangle()
    right(5)
