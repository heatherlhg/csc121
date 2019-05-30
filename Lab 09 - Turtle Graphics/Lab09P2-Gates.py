# Lab 09 - Turtle Graphics - Problem 2
# Heather Gates

# Write a Python program that uses Turtle Graphics to draw the letter “M” with four lines.
# Decide the size and the location of the letter yourself.

import turtle
turtle.setup(500, 500)

turtle1 = turtle.Turtle()
turtle1.color('pink')
turtle1.pensize(8)
turtle1.setposition(0, 200)
turtle1.setposition(100, 100)
turtle1.setposition(200,200)
turtle1.setposition(200, 0)
turtle1.hideturtle()

turtle.exitonclick()
