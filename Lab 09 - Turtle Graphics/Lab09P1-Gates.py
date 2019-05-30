# Lab 09 - Turtle Graphics - Problem 1
# Heather Gates

# Write a Python program that uses Turtle Graphics to draw the letter “E” with four lines.
# Decide the size and the location of the letter yourself.

import turtle
turtle.setup(500, 500)

turtle1 = turtle.Turtle()
turtle1.color('blue')
turtle1.pensize(8)
turtle1.setposition(-160, 0)
turtle1.setposition(-160, 200)
turtle1.setposition(0,200)
turtle1.penup()
turtle1.setposition(-40, 100)
turtle1.pendown()
turtle1.setposition(-160, 100)
turtle1.hideturtle()

turtle.exitonclick()
