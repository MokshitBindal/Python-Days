import time
from turtle import Turtle, Screen

ALIGNMENT = 'center'
FONT = ('Courier', 50, 'normal')

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        # self.setheading(UP)
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        # self.setheading(UP)
        # self.forward(5)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

class ScoreBoard(Turtle):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.score = 0
        self.penup()
        self.color("white")
        if self.player == "r":
            self.goto(100, 200)
        elif self.player == "l":
            self.goto(-100, 200)
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()
        self.print_score()

    def print_score(self):
        self.write(self.score, move=False,
                   align=ALIGNMENT, font=FONT)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.ball_speed = 1
        self.speed(self.ball_speed)
        # self.setheading(35)
        self.penup()
        self.x_move = 10
        self.y_move = 10


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        # self.ball_speed += 1
        # self.speed(self.ball_speed)

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed += 1
        self.speed(self.ball_speed)

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.speed(1)

def section_maker():
    # y_pos = [-500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500]
    y_pos = [position for position in range(-280, 281, 40)]
    all_sections = []

    for section_index in range(len(y_pos)):
        new_section = Turtle(shape="square")
        new_section.color("white")
        new_section.penup()
        new_section.shapesize(stretch_len=0.35, stretch_wid=0.9)
        new_section.goto(x=0, y=y_pos[section_index])
        all_sections.append(new_section)

screen = Screen()
r_score = ScoreBoard("r")
l_score = ScoreBoard("l")
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

section_maker()

ball = Ball()
screen.update()
screen.listen()

# screen.onkey(r_paddle.up, "Up")
# screen.onkey(r_paddle.down, "Down")
# screen.onkey(l_paddle.up, "w")
# screen.onkey(l_paddle.down, "s")

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

r_score.print_score()
l_score.print_score()

is_game_on = True
while is_game_on:
    time.sleep(0.01)
    screen.tracer(1)
    # screen.update()
    ball.move()

    # detect wall collision and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle and bounce
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # check if ball is out of bounds

    if ball.xcor() > 380:
        l_score.update_score()
        screen.tracer(0)
        ball.reset()
        # screen.update()
        screen.tracer(1)

    elif ball.xcor() < -380:
        r_score.update_score()
        screen.tracer(0)
        ball.reset()
        screen.tracer(1)

screen.exitonclick()
