from turtle import *

length = 100
def star(length):
    for i in range(5):
        forward(length)
        right(144)

def star_function():
    length = 100
    for i in range(100):
        speed(0)
        length += 5
        right(5)
        star(length)

star_function()