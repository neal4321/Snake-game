from turtle import Turtle
import snake as s

score = 0

score_turtle = Turtle()
score_turtle.hideturtle()
score_turtle.up()
score_turtle.color("white")
score_turtle.goto(0, 260)


def snake_score():
    global score
    score += 10
    update_score(score)
    s.create_turtle(shape="square", position=s.snake[-1].pos(), list=s.snake, heading=s.snake[-1].heading())


def update_score(score):
    score_turtle.clear()
    score_turtle.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))


update_score(score)
