from turtle import*

def trig():
    for counter in range(3):
        fd(50)
        right(240)

def pentg():
    for counter in range(5):
        fd(100)
        right(72)

def hexg():
    for counter in range(6):
        fd(100)
        right(60)

def square():
    for counter in range (4):
        fd(200)
        right(90)

def envelope():
    square()
    right(45)
    fd(140)
    left(90)
    fd(140)

trig()
pentg()
hexg()
envelope()

