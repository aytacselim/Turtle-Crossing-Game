from turtle import Turtle

POSITIONS = [(-300, 280), (-300, -260)]


class Lines(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        for position in POSITIONS:
            self.goto(position)
            drawing = True
            while drawing:
                self.pendown()
                self.forward(10)
                self.penup()
                self.forward(10)
                if self.xcor() > 300:
                    drawing = False
