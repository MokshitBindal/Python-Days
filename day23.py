import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Road Crossing Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Create player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.shapesize(1)
player.penup()
player.goto(0, -250)

# Create cars
cars = []


def create_car():
    car = turtle.Turtle()
    car.shape("square")
    car.color("red")
    car.shapesize(1, 2)
    car.penup()
    y = random.randint(-200, 200)
    car.goto(300, y)
    return car

# Move the player


def move_up():
    y = player.ycor()
    player.sety(y + 20)


def move_down():
    y = player.ycor()
    player.sety(y - 20)


# Keyboard bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

# Main game loop
while True:
    # Create a car with a certain probability
    if random.random() < 0.2:
        new_car = create_car()
        cars.append(new_car)

    # Move each car
    for car in cars:
        x = car.xcor()
        car.setx(x - 10)

        # Check for collision with player
        if player.distance(car) < 20:
            player.goto(0, -250)

        # Remove cars that have moved off the screen
        if x < -300:
            car.hideturtle()
            cars.remove(car)

    # Update the screen
    screen.update()
    time.sleep(0.1)

# Uncomment the line below if you want to run the turtle main loop
turtle.mainloop()
