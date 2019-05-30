# Lab 09 - Turtle Graphics - Problem 3
# Heather Gates

# Write a Python program that uses Turtle Graphics to draw the letters “XYZ” with straight lines.
# Decide the size and the location of the letters yourself.

import turtle
turtle.setup(1000, 500)

turtle1 = turtle.Turtle()
turtle1.color('orange')
turtle1.pensize(8)

# Letter X
turtle1.penup()
turtle1.setposition(-160, 0)
turtle1.pendown()
turtle1.setposition(-400, 200)
turtle1.penup()
turtle1.setposition(-400,0)
turtle1.pendown()
turtle1.setposition(-160, 200)

# Letter Y
turtle1.penup()
turtle1.setposition(-120, 200)
turtle1.pendown()
turtle1.setposition(0, 120)
turtle1.setposition(0, 0)
turtle1.penup()
turtle1.setposition(0, 120)
turtle1.pendown()
turtle1.setposition(120, 200)

# Letter Z
turtle1.penup()
turtle1.setposition(160, 200)
turtle1.pendown()
turtle1.setposition(400, 200)
turtle1.setposition(160, 0)
turtle1.setposition(400, 0)

turtle1.hideturtle()

turtle.exitonclick()
