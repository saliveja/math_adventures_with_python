from turtle import *

length = 5
def turtle_spiral(length):

    for i in range(4):
        right(90)
        forward(length)


for i in range(61):
    right(5)
    length += 5
    turtle_spiral(length)

