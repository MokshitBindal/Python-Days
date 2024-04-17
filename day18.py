from turtle import Turtle, Screen, colormode
import random

# from turtle import *
# import turtle as t

# colors = ["dark red", "forest green",
#           "medium blue", "indigo", "magenta", "dim gray"]

tim = Turtle()
tim.shape("classic")
# tim.color("bisque4")

# # for turtle colors 
# # https://cs111.wellesley.edu/reference/colors
# # https://trinket.io/docs/colors

# tim.width(10)
# tim.forward(100)
# tim.color("red")
# tim.right(45)
# tim.forward(100)


# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# for i in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# total_angle = 360
# no_of_edges = 3

# for j in range(3,11):
#     tim.color(choice(colors))
#     for i in range(no_of_edges):
#         tim.right(total_angle/no_of_edges)
#         tim.forward(100)
#     no_of_edges += 1


# tim.speed(0) 
# # tim.speed("fastest")
# tim.pensize(15)
# direction = [0, 90, 180, 270]

# for i in range(100):
#     color = random.choice(colors)
#     tim.color(color)
#     direc = random.choice(direction)

#     tim.setheading(direc)
#     tim.forward(40)


# colormode(255)
# tim.speed(0)
# tim.pensize(15)
# direction = [0, 90, 180, 270]

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

# for i in range(200):
#     tim.pencolor(random_color())
#     direc = random.choice(direction)

#     tim.setheading(direc)
#     tim.forward(40)

# colormode(255)
# tim.speed(0)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

# for i in range(int(360/5)):
#     tim.pencolor(random_color())
#     tim.circle(200)
#     # current_heading = tim.heading()
#     # tim.setheading(current_heading + 5)
#     tim.left(5)


# import colorgram

# colors = colorgram.extract(
#     "/home/mokshitbindal/Documents/Programming_files/Python/Programs/Projects/Hirst_painting/image.jpg", 30)

# color_list = []
# for i in range(30):
#     first_color = colors[i]
#     # r = first_color.rgb.r
#     # g = first_color.rgb.g
#     # b = first_color.rgb.b
#     rgb = first_color.rgb
#     red = rgb[0]
#     green = rgb[1]
#     blue = rgb[2]
#     color_list.append((red, green, blue))

# print(color_list)


tim = Turtle()

colors_rgb = [
    (213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171),
    (124, 79, 99), (122, 175, 156), (226, 198, 131), (192, 87, 108), (11, 50, 64),
    (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29),
    (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171),
    (170, 23, 18), (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185),
    (49, 62, 84)
]

colormode(255)
tim.speed(0)
y = 0
for height in range(10):
    for width in range(10):
        tim.dot(20, random.choice(colors_rgb))
        tim.penup()
        tim.forward(50)
        # print(tim.pos())
    y += 50
    tim.setpos(0, y)
tim.hideturtle()


screen_1 = Screen()
screen_1.exitonclick()
