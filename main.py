from turtle import Screen, Turtle
import time
import snake as s
import food as f

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Serpent")
screen.tracer(0)

s.create_snake()


def left_turn():
    global turn_hold
    if not turn_hold:
        s.snake[0].left(90)
        turn_hold = True

def right_turn():
    global turn_hold
    if not turn_hold:
        s.snake[0].right(90)
        turn_hold = True



screen.listen()
screen.onkey(key="a", fun=left_turn)
screen.onkey(key="d", fun=right_turn)
game_in_progress = True
while game_in_progress:
    speed = s.snake_speed()
    f.check_food()
    turn_hold = False
    game_in_progress = s.move()
    screen.update()
    time.sleep(speed)

screen.exitonclick()
