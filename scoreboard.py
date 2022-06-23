from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        with open("data.txt") as data:
            self.high_score = data.read()
        self.goto(0, 278)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        with open("data.txt", mode="r") as high_score:
            new_score = int(high_score.read())
            if self.score > new_score:
                with open("data.txt", mode="w") as current_score:
                    current_score.write(f"{self.score}")
                    self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.penup()
    #     self.hideturtle()
    #     self.goto(0, 0)
    #     self.write(arg="Game Over", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()
