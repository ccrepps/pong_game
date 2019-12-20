# Pong game by Nuwanduhhh

import turtle
import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height= 600)
wn.tracer(0)

# Score Variant
score_a: int = 0
score_b = 0


# Title
title = turtle.Turtle()
title.speed(0)
title.color("white")
title.penup()
title.hideturtle()
title.goto(0, 260)
title.write("PONG", font=("Courier", 24, "normal"), align="center")

# Winner Prompt
win_O = turtle.Turtle()
win_O.speed(0)
win_O.color("orange")
win_O.penup()
win_O.hideturtle()
win_O.goto(0, 150)


win_B = turtle.Turtle()
win_B.speed(0)
win_B.color("blue")
win_B.penup()
win_B.hideturtle()
win_B.goto(0, 150)



# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(10)
paddle_a.shape("square")
paddle_a.color("orange")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(10)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(10)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .15
ball.dy = .15

# Team Names
orange = turtle.Turtle()
orange.speed(0)
orange.color("white")
orange.penup()
orange.ht()
orange.goto(-260, 260)
orange.write("Orange Team", align='center', font=("Courier", 18, "italic"))

blue = turtle.Turtle()
blue.speed(0)
blue.color("white")
blue.penup()
blue.ht()
blue.goto(260, 260)
blue.write("Blue Team", align='center', font=("Courier", 18, "italic"))

# Score
pen_O = turtle.Turtle()
pen_O.speed(0)
pen_O.color("orange")
pen_O.penup()
pen_O.hideturtle()
pen_O.goto(-260, 220)
pen_O.write("0", align= 'center', font=("Times", 22, "normal"))

pen_B = turtle.Turtle()
pen_B.speed(0)
pen_B.color("Blue")
pen_B.penup()
pen_B.hideturtle()
pen_B.goto(260, 220)
pen_B.write("0", align= 'center', font=("Times", 22, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")

wn.listen()
wn.onkeypress(paddle_a_down, "s")

wn.listen()
wn.onkeypress(paddle_b_up, "Up")

wn.listen()
wn.onkeypress(paddle_b_down, "Down")








# Main game loop
while True:
    wn.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -291:
        ball.sety(-291)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen_O.clear()
        pen_O.write(str(score_a), align='center', font=("Times", 22, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen_B.clear()
        pen_B.write(str(score_b), align='center', font=("Times", 22, "normal"))


    # Paddle and Ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1



    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    if score_a >= 5:
        ball.dx = 0
        ball.dy = 0
        win_O.write("Orange Wins", font=("Courier", 24, "normal"), align="center")
        turtle.Screen().exitonclick()

    if score_b >= 5:
        ball.dx = 0
        ball.dy = 0
        win_B.write("Blue Wins", font=("Courier", 24, "normal"), align="center")
        turtle.Screen().exitonclick()
