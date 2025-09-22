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

ShapeOrStar=input("are u drawing a SHAPE or STAR? ")
ShapeOrStar=ShapeOrStar.lower()
ShapeOrStar=str(ShapeOrStar)
print()
print("if star,know stars with an even amount of points look weird")
sides=input("how many sides/points are there? ")
sides=int(sides)
print()
length=input("what is the length of each side? ")
length=int(length)
angle=(360/sides)
           
def DrawShapeOrStar():
    if ShapeOrStar=="shape":
        for counter in range(sides):
            fd(length)
            right(angle)
    elif ShapeOrStar=="star":
        for counter in range(sides):
            fd(length)
            right(180+0.5*angle) #this formula only works for odd numbers
    
DrawShapeOrStar()
