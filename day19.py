# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# # here we are using fuction as an input in calculate
# # calculate is a high order function that means that it works with other functions

# def calculate(n1, n2, func):
#     return func(n1, n2)

# calculate(3,5,add)
# calculate(3,5,subtract)


from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()
'''
screen.listen()

def move_forward():
    tim.forward(20)

screen.onkey(key = "space", fun = move_forward) 
'''
# we are not writing move_forward() as it is under a high order function,
# we can understand it as
# writing move_forward() means you want to execute it right now but we want
# to execute when space is pressed

'''
def move_backward():
    tim.backward(20)

def move_forward():
    tim.forward(20)

def counter_clockwise():
    # current_heading = tim.heading()
    # tim.setheading(current_heading + 10)
    tim.left(10)

def clockwise():
    # current_heading = tim.heading()
    # tim.setheading(current_heading - 10)
    tim.right(10)

def clear_screen():
    tim.reset()
    # tim.clear()
    # tim.penup()
    # tim.home()
    # tim.pendown()

screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = counter_clockwise)
screen.onkey(key = "d", fun = clockwise)
screen.onkey(key = "c", fun = clear_screen)
'''
# turtle_1 = Turtle(shape="turtle")
# turtle_2 = Turtle(shape="turtle")
# turtle_3 = Turtle(shape="turtle")
# turtle_4 = Turtle(shape="turtle")
# turtle_5 = Turtle(shape="turtle")
# turtle_6 = Turtle(shape="turtle")

# screen = Screen()
# screen.setup(width=500, height=400)

# turtle_1.penup()
# turtle_2.penup()
# turtle_3.penup()
# turtle_4.penup()
# turtle_5.penup()
# turtle_6.penup()

# user_bet = screen.textinput(title="Make your bet",
#                             prompt="Which Turtle will win the race? Enter a colour[blue/green/cyan/red/orange/purple]: ")
# print(user_bet)

# colours = ["blue", "green", "purple", "red", "cyan", "orange"]

# i = 0
# for turtle in screen.turtles():
#     turtle.color(colours[i])
#     i += 1

# turtle_1.goto(x = -230, y = -150)
# turtle_2.goto(x =-230, y= -90)
# turtle_3.goto(x =-230, y= -30)
# turtle_4.goto(x =-230, y= 30)
# turtle_5.goto(x =-230, y= 90)
# turtle_6.goto(x =-230, y= 150)

import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet",
                            prompt="Which Turtle will win the race? Enter a colour[blue/green/cyan/red/orange/purple]: ")

colours = ["blue", "green", "purple", "red", "cyan", "orange"]
y_pos = [-150, -90, -30, 30, 90, 150]
all_turtles = []

# rather than creating multiple objects, we used a for loop to create a object in each iteration
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

# our turtle is 40*40 figure thus 230 is used by us
while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle has won the race!")
            else:
                print(f"You've lost! The {winning_color} turtle has won the race!")

        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)


screen.exitonclick()
