# from turtle import Turtle, Screen

# my_turtle = Turtle()
# my_screen = Screen()
# print(my_turtle)
# my_turtle.shape("turtle")
# my_turtle.color("red")
# my_turtle.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()

# my_screen is a object here, object are like a system eg. car orobject human
# canvheight is the attribute of the object,
# attributes are the things object has like car has wheels or music system
# methods are the things that an object can do


from prettytable import PrettyTable

Table = PrettyTable()
Table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"])
Table.add_column("Type", ["Electric", "Water", "Fire"])
Table.align["Type"] = "l"
print(Table)
