from turtle import*

#this drawns a triangle
#def trig():
  #  for counter in range(3):
#        fd(50)
#        right(240)

#this drawns a pentagon
#def pentg():
#    pencolor("red")
#    for counter in range(5):
#        fd(100)
#        right(72)

#this drawns a hexagon
#def hexg():
#    pencolor("green")
#    for counter in range(6):
#        fd(100)
#        right(60)

#this drawns a square for the envelope
#def square():
#    for counter in range (4):
#        fd(200)
#        right(90)

#this drawns an envelope
#def envelope():
#    pencolor("pink")
#    square()
#    right(45)
#    fd(140)
#    left(90)
#    fd(140)

#trig()
#pentg()
#hexg()
#envelope()
#square is in envelope




#Task 1: Look at the following code and decide which picture it will generate.
#Then download it from the shared drive, then save and run it, to check.

#def demo():
#  pencolor("red")
#  for counter in range (18):
#    forward (350)
#    right(100)

#demo()

#20 pount star?
#18 points

#def manypointstar():
#    pencolor("pink")
#    for counter in range(400):
#        fd(400)
#        right(179)

#manypointstar()


#def petal():
#    for counter in range(200):
#        circle(200,359)
#        left(60)
#        circle(200,359)

#petal()

length=input("what is the length of each side? ")
length=int(length)
angle=input("at what angle is each side? ")
angle=length(angle)

def drawshape():
    right(angle)
    fd(length)