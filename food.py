import snake as s

food_in_play = False

def check_food():
    global food_in_play
    if not food_in_play:
        for turtle in s.food:
            turtle.hideturtle()
        s.food = []
        food_in_play = s.spawn_food()
