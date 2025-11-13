# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle
import math
import time
import random


def set_background(image_filename):
    screen = turtle.Screen()
    try:
        screen.bgpic(
            f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(
            f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")


def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)


def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x, y)
    window.update()
    return sprite


def get_distance(s1, s2):
    dx = s1.xcor() - s2.xcor()
    dy = s1.ycor() - s2.ycor()
    return math.sqrt(dx*dx + dy*dy)


def draw_rectangle(color="black", x=0, y=0, width=100, height=100,):
    sprite = turtle.Turtle()
    sprite.speed(0)
    sprite.pencolor(color)
    sprite.color(color)
    sprite.penup()
    sprite.goto(x - (width*0.5), y + (height*0.5))
    sprite.pendown()
    sprite.begin_fill()
    for i in range(2):
        sprite.forward(width)
        sprite.right(90)
        sprite.forward(height)
        sprite.right(90)
    sprite.end_fill()
    sprite.hideturtle()


window = turtle.Screen()
window.tracer(0)


# Section 2: Setup
s1 = create_sprite("Thief", -0, 0)

s2 = create_sprite("night_gard", 200, -200)

s3 = create_sprite("blacksquare", random.randint(-300, 300),
                   random.randint(-300, 300))
s4 = create_sprite("blacksquare", random.randint(-300, 300),
                   random.randint(-300, 300))
s5 = create_sprite("blacksquare", random.randint(-300, 300),
                   random.randint(-300, 300))
s6 = create_sprite("blacksquare", random.randint(-300, 300),
                   random.randint(-300, 300))
s7 = create_sprite("blacksquare", random.randint(-300, 300 ),
                    random.randint(-300, 300))

set_background("black (1)")

tags = 0
# Section 3: Controls


def can_i_move_up(s1, blacksquare):
    if abs(s1.xcor() - blacksquare.xcor()) > 30:
        return True
    if s1.ycor() > blacksquare.ycor():
        return True
    if s1.ycor() < blacksquare.ycor() - 100:
        return True
    return False


def move_up():
    s1.setheading(90)


    if can_i_move_up(s1, s3) and can_i_move_up(s1,s4) and can_i_move_up(s1,s5) and can_i_move_up(s1,s6) and can_i_move_up(s1,s7):
        s1.forward(10)


window.onkeypress(move_up, "w")

def can_i_move_down(s1, blacksquare):
    if abs(s1.xcor() - blacksquare.xcor()) > 30:
        return True
    if s1.ycor() > blacksquare.ycor():
        return True
    if s1.ycor() < blacksquare.ycor() - 10:
        return True
    return False

def move_down():
    s1.setheading(270)
    if can_i_move_down(s1, s3) and can_i_move_down(s1,s4) and can_i_move_down(s1,s5) and can_i_move_down(s1,s6) and can_i_move_down(s1,s7):
        s1.forward(10)


window.onkeypress(move_down, "s")

def can_i_move_left(s1, blacksquare):
    if abs(s1.xcor() - blacksquare.xcor()) > 30:
        return True
    if s1.ycor() > blacksquare.ycor():
        return True
    if s1.ycor() < blacksquare.ycor() - 10:
        return True
    return False

def move_left():
    s1.setheading(180)
    if can_i_move_left(s1, s3) and can_i_move_left(s1,s4) and can_i_move_left(s1,s5) and can_i_move_left(s1,s6) and can_i_move_left(s1,s7):
    	s1.forward(10)


window.onkeypress(move_left, "a")

def can_i_move_right(s1, blacksquare):
    if abs(s1.xcor() - blacksquare.xcor()) > 30:
        return True
    if s1.ycor() > blacksquare.ycor():
        return True
    if s1.ycor() < blacksquare.ycor() - 10:
        return True
    return False

def move_right():
    s1.setheading(0)
    if can_i_move_right(s1, s3) and can_i_move_right(s1,s4) and can_i_move_right(s1,s5) and can_i_move_right(s1,s6) and can_i_move_right(s1,s7):
    	s1.forward(10)


window.onkeypress(move_right, "d")

#gard controls

def can_i_move_up(s2, blacksquare):
    if abs(s1.xcor() - blacksquare.xcor()) > 30:
        return True
    if s2.ycor() > blacksquare.ycor():
        return True
    if s2.ycor() < blacksquare.ycor() - 10:
        return True
    return False


def move_up():
    s2.setheading(90)
    if can_i_move_up(s2, s3) and can_i_move_up(s2,s4) and can_i_move_up(s2,s5) and can_i_move_up(s2,s6) and can_i_move_up(s2,s7):
    	s2.forward(10)


window.onkeypress(move_up, "Up")

def can_i_move_down(s1, blacksquare):
    if abs(s2.xcor() - blacksquare.xcor()) > 30:
        return True
    if s2.ycor() > blacksquare.ycor():
        return True
    if s2.ycor() < blacksquare.ycor() - 10:
        return True
    return False

def move_down():
    s2.setheading(270)
    if can_i_move_down(s2, s3) and can_i_move_down(s2,s4) and can_i_move_down(s2,s5) and can_i_move_down(s2,s6) and can_i_move_down(s2,s7):
    	s2.forward(10)


window.onkeypress(move_down, "Down")

def can_i_move_left(s1, blacksquare):
    if abs(s2.xcor() - blacksquare.xcor()) > 30:
        return True
    if s2.ycor() > blacksquare.ycor():
        return True
    if s2.ycor() < blacksquare.ycor() - 10:
        return True
    return False

def move_left():
    s2.setheading(180)
    if can_i_move_left(s2, s3) and can_i_move_left(s2,s4) and can_i_move_left(s2,s5) and can_i_move_left(s2,s6) and can_i_move_left(s2,s7):
   		s2.forward(10)


window.onkeypress(move_left, "Left")

def can_i_move_right(s1, blacksquare):
    if abs(s2.xcor() - blacksquare.xcor()) > 30:
        return True
    if s2.ycor() > blacksquare.ycor():
        return True
    if s2.ycor() < blacksquare.ycor() - 10:
        return True
    return False

def move_right():
    s2.setheading(0)
    if can_i_move_right(s2, s3) and can_i_move_right(s2,s4) and can_i_move_right(s2,s5) and can_i_move_right(s2,s6) and can_i_move_right(s2,s7):
    	s2.forward(10)


window.onkeypress(move_right, "Right")

# Section 4: Game Loop
window.listen()
timer = 0
while True:
    time.sleep(1)
    timer += 1

    # TODO - code for automatic actions

    window.update()

    if timer == 60 or get_distance(s1, s2) < 50:
        break


print("Game Over")
