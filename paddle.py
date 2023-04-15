from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        new_Y = self.ycor() + 20
        self.goto(self.xcor(), new_Y)

    def go_down(self):
        new_Y = self.ycor() - 20
        self.goto(self.xcor(), new_Y)
