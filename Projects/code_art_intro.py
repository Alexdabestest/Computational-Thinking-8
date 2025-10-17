# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("purple")
t.pendown()

for i in range(6):
    t.forward(100)
    t.left(140)
    t.forward(100)
    t.left(-70)
    t.forward(100)
    t.left(130)

# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
