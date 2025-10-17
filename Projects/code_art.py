#this brings the turtle into my code
import turtle
t = turtle.Turtle()

t.penup()
t.goto(0, 0)
#my differant colors
colors = ["Indigo", "DarkBlue", "Navy", "MidnightBlue"]
t.pendown()

#this is the code to move everything around
for i in range(182):
    t.color( colors[i % 4] )
    t.forward(50 + i)
    t.left(90 +1)

turtle.exitonclick()