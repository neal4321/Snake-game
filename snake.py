from turtle import Turtle
import score
import food as f
from random import randint as r

snake = []
food = []

def create_turtle(shape, position, list, heading):
    new_turtle = Turtle(shape=shape)
    new_turtle.up()
    new_turtle.color("white")
    new_turtle.goto(position)
    new_turtle.setheading(heading)
    list.append(new_turtle)

def create_snake():
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    for position in starting_positions:
        create_turtle(shape="square", position=position, list=snake, heading=0)

def move():
    proceed = True
    for segment in snake:
        if not f.food_in_play:
            if segment != snake[-1]:
                segment.forward(20)
        else:
            segment.forward(20)
        current_heading = segment.heading()
        if segment != snake[0]:
            segment.setheading(next_segment_heading)
        next_segment_heading = current_heading

        if segment == snake[0]:
            proceed, f.food_in_play = check_object_collision()

    if proceed:
        return check_wall_collision(snake[0])
    else:
        return False


def check_object_collision():
    for segment_check in snake:
        if segment_check != snake[0]:
            distance = snake[0].distance(segment_check)
            if distance < 1:
                return False, True
    for food_check in food:
        food_distance = snake[0].distance(food_check)
        if food_distance < 1:
            score.snake_score()
            return True, False
    return True, True


def check_wall_collision(snake_head):
    if snake_head.xcor() >= 300 or snake_head.xcor() <= -300 or \
            snake_head.ycor() >= 260 or snake_head.ycor() <= -300:
        return False
    else:
        return True

def snake_speed():
    if score.score >= 150:
        return 0.05
    elif score.score >= 100:
        return 0.1
    elif score.score >= 50:
        return 0.2
    elif score.score >= 20:
        return 0.3
    else:
        return 0.5


def spawn_food():
    x_coord = r(-14, 14)*20
    y_coord = r(-14, 12)*20
    new_food = Turtle(shape="circle")
    new_food.up()
    new_food.color("white")
    new_food.goto((x_coord, y_coord))
    food.append(new_food)
    return True

