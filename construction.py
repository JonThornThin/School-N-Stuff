#Bob; The Builder

from turtle import *
speed(2)
# drawing a house
from turtle import *

length=int(input("length? "))

def square():
    for counter in range(4):
        fd(length)
        right(90)

def triangle():
    color("red")
    for counter in range(3):
        forward(length)
        left(120)
        
def house():
    square()
    triangle()
    penup()
    neglength=int(0-length)
    halflength=int(0.3*length)
    setposition(halflength, neglength)
    pendown()
    for counter in range(4):
        fd(length*0.3)
        left(90)
house()

