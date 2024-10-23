from turtle import Turtle
import random

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.x_move = 10 * random.choice([1, -1])  
        self.y_move = 10 * random.choice([1, -1])  
        self.move_speed = 0.5
        self.speed_factor = 1  # faktor för att exponentiellt öka hastigheten

    def move(self):
        new_x = self.xcor() + self.x_move * self.speed_factor
        new_y = self.ycor() + self.y_move * self.speed_factor
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.increase_speed()

    def increase_speed(self):
        """Ökar hastigheten exponentiellt."""
        self.speed_factor *= 1.1  # ökar hastigheten med 10% varje gång

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.5
        self.speed_factor = 1  # återställ hastigheten
        self.x_move *= random.choice([1, -1]) 
        self.y_move *= random.choice([1, -1])   

