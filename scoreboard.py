from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highScore = 0
        self.hideturtle()
        self.setpos(x=0, y=270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highScore}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.penup()
    #     self.home()
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
        self.score = 0
        self.update_scoreboard()

