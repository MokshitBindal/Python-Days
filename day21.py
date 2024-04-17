class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

# Inheritence


class Fish(Animal):

    def __init__(self):
        super().__init__()
        # inherits everything from the super class: Animal like variables and functions

    def breathe(self):
        super().breathe()  # can declare this independently of super_init
        print("Fish breathing underwater")

    def swim(self):
        print("Swimming in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_of_eyes)

# slicing lists and tuples
list1 = ["h", "i", "v", "j", "k", "l", "y"]
tup1 = ("h", "i", "v", "j", "k", "l", "y")
# starting_index: ending_index(not included last): step
print(list1[1:5:2])
print(tup1[3:1:-1])
