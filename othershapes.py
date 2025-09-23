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

ShapeOrStar=str(input("are u drawing a SHAPE or STAR? "))
ShapeOrStar=ShapeOrStar.lower() #ignore capitalisATION FOR VAR
print()
print("if star, know stars with an even amount of points look weird")
sides=int(input("how many sides/points are there? "))
print()
length=int(input("what is the length of each side? ")) #int and input on same line wow so good
angle=(360/sides) #formula for angles to work
           
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