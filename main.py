from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)

    # Skapa paddlarna
    left_paddle = Paddle((-350, 0))
    right_paddle = Paddle((350, 0))

    # Skapa boll och scoreboard
    ball = Ball()
    scoreboard = Scoreboard()

    # Funktion för att registrera rörelse
    def move_left_paddle_up():
        left_paddle.move_up()
    
    def move_left_paddle_down():
        left_paddle.move_down()

    def move_right_paddle_up():
        right_paddle.move_up()

    def move_right_paddle_down():
        right_paddle.move_down()

    # Lyssna på tangenttryck och starta rörelsen
    screen.listen()
    screen.onkeypress(move_left_paddle_up, "w")
    screen.onkeypress(move_left_paddle_down, "s")
    screen.onkeypress(move_right_paddle_up, "Up")
    screen.onkeypress(move_right_paddle_down, "Down")

    # Huvudloop för spelet
        # Huvudloop för spelet
    game_is_on = True
    while game_is_on:
        time.sleep(3 * ball.move_speed)  # Uppdatera sömn baserat på hastighet
        screen.update()
        ball.move()

        # Studsa mot över- och underkanten
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.bounce_y()

        # Studsa mot paddlarna
        if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        # Om bollen går förbi höger paddel
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()

        # Om bollen går förbi vänster paddel
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()


    screen.exitonclick()

if __name__ == "__main__":
    main()
