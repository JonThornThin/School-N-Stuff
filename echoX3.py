#Call it echo echo echo

# program written for Session 4

from turtle import *

# this line says we are using the "turtle" library of functions
# remember to use this for turtle graphics in Python


def star():
    fillcolor("Purple")
    begin_fill()
    pencolor("Red")
    for counter in range (5):
        forward (300) 
        left(216)
    
def trisqr():
    fillcolor("Purple")
    begin_fill()
    pencolor("Orange")
    for counter in range(4):
        forward(50)
        right(90)
    penup()
    fd(100)
    pendown()
    for counter in range(3):
        fd(50)
        right(240)
              
def ringrondrus():
    pencolor("Green")
    circle(50)
    penup()
    right(90)
    fd(50)
    left(90)
    pendown()
    circle(100)

def manyatring():
    pencolor("Blue")
    fd(50)
    for counter in range(6):
        right(240)
        fd(50)
        right(240)
        fd(50)
        right(300)
        fd(50)

def bigstar():
    fillcolor("Purple")
    begin_fill()
    pencolor("Purple")
    backward(100)
    for counter in range(8):
        forward(300) 
        left(225)
    
star()
trisqr()
ringrondrus()
manyatring()
bigstar()

def square():
    for counter in range(4):
        forward(100)
        right(90)

#for i in range(8):
#    square()
#    left(45)

#122 lines be there
    
def house():
    for counter in range (4):
        fd(100)
        right(90)
    left(45)
    fd(73)
    right(90)
    fd(73)
house()