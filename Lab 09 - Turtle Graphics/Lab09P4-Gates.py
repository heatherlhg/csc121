# Lab 09 - Turtle Graphics - Problem 4
# Heather Gates

# Write a Python program that shows a turtle walking back and forth between two vertical walls.  Please do the following:

# (a)	Create a 800 X 600 Turtle Graphics window
import turtle
turtle.setup(800, 600)

# set wall coordinates
left = -300
right = 300
top = 200
bottom = -200

# (b)	Draw a vertical line at x-coordinate = -300.  The y-coordinates of the two end points are 200 and -200, respectively.
turtle1 = turtle.Turtle()
turtle1.color('gray')
turtle1.pensize(5)
turtle1.penup()
turtle1.setposition(left, top)
turtle1.pendown()
turtle1.setposition(left, bottom)

# (c)	Draw another vertical line at x-coordinate = 300.  The y-coordinates of the two end points are 200 and -200, respectively.
turtle1.penup()
turtle1.setposition(right, bottom)
turtle1.pendown()
turtle1.setposition(right, top)
turtle1.hideturtle()

# (d)	Create a turtle object and change the shape from arrowhead to turtle.
turtle2 = turtle.Turtle()
turtle2.shape('turtle')
turtle2.color('green')

# (e)	Use a loop to make the turtle walk 2000 steps.  Whenever the turtle hits a wall, it turns 180 degree and continues to walk.
for i in range(2000):
    turtle2.forward(1)
    if turtle2.xcor() >= right or turtle2.xcor() <= left:
        turtle2.left(180)

turtle.exitonclick()
