from turtle import*

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

sides=input("how many sides are there? ")
sides=int(sides)
length=input("what is the length of each side? ")
length=int(length)
angle=input("at what angle is each side? ")
angle=int(angle)

def drawshape():
    for counter in range(sides):
        fd(length)
        right(angle)
    
drawshape()
