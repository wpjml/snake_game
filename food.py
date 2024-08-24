import random
import turtle


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.goto(random.randint(-270, 270), random.randint(-270, 270))

    def refresh(self):
        self.goto(random.randint(-270, 270), random.randint(-270, 270))
