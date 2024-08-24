import turtle


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def score_write(self):
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.clear()
        self.write(f"SCORE: {self.score}", False, "center", ("Arial", 20, "normal"))

    def score_check(self):
        self.score += 1

    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Arial", 30, "normal"))
