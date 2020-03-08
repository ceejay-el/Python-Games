#Simple Pong Game

import turtle

page = turtle.Screen()
page.title("Pong")
page.bgcolor("black")
page.setup(width = 800, height = 600)
page.tracer(0)

#keeping scores for game
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()        #prevents turtle from drawing line as it moves
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .1
ball.dy = -.1

#Pen...Turtle?
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0      Player B: 0", align="center", font=("Arial", 16, "normal"))

#FUNCTIONS
#Move paddles up and down
def paddle_a_Up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_Down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_Up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_Down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding
page.listen()
page.onkeypress(paddle_a_Up, "w")
page.onkeypress(paddle_a_Down, "s")
page.onkeypress(paddle_b_Up, "Up")
page.onkeypress(paddle_b_Down, "Down")


# Main game loop
while True:
    page.update()

    #Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    #Top and bottom borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #Right and left borders
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(score_a, score_b), align="center", font=("Arial", 16, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(score_a, score_b), align="center", font=("Arial", 16, "normal"))

    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
