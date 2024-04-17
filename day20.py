from turtle import Screen, Turtle
# from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
# all_turtles = []
# starting_positions = [(0,0), (-20,0), (-40,0)]

# for position in starting_positions:
#     new_turtle = Turtle(shape="square")
#     new_turtle.color("white")
#     new_turtle.penup()
#     new_turtle.goto(position)
#     all_turtles.append(new_turtle)

# screen.update()
while True:
    screen.update()
    time.sleep(1)

    snake.move()
    # for turtle in range(len(all_turtles)-1, 0, -1):
    #     new_x = all_turtles[turtle-1].xcor()
    #     new_y = all_turtles[turtle-1].ycor()
    #     all_turtles[turtle].goto(new_x, new_y)
    # all_turtles[0].forward(20)

screen.exitonclick()