from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Keyboard bindings
screen.listen()  # Set the screen to listen for key presses
screen.onkeypress(r_paddle.go_up, "Up")  # Bind the Up arrow key to the r_paddle.go_up function
screen.onkeypress(r_paddle.go_down, "Down")  # Bind the Down arrow key to the r_paddle.go_down function
screen.onkeypress(l_paddle.go_up, "w")  # Bind the W key to the l_paddle.go_up function
screen.onkeypress(l_paddle.go_down, "s")  # Bind the S key to the l_paddle.go_down function

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    # Detect R paddle misses 
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L Psddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()