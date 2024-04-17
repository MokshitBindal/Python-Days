# FileNotFoundError
# with open("file.txt") as f:
#     f.read()

# KeyError
# a_dict = {"key": "value"}
# value = a_dict["not_a_key"]

# IndexError
# list1 = ["apples", "cheese", "banana"]
# list1[3]

# TypeError
# text = "abc"
# print(text + 5)


# Catching Exceptions Basic Format
# try: something that may cause exception/error
# except: do this if there was a error
# else: do this if there was no error
# finally: do this no matter what happens


# try:
#     f = open("file.txt", "r")
# except: # Dont use bare except clause
#     print("File not found")
#     f = open("file.txt", "w")
#     f.write("Hello, world!")
# else:
#     print("File found")
# finally:
#     data = f.read()
#     print(data)
#     f.close()


# try:
#     f = open("file.txt", "r")
#     a_dict = {"key": "value"}
#     # value = a_dict["not_a_key"]
#     print(a_dict["key"])
# except FileNotFoundError:
#     print("Creating Your file with required data, restart please")
#     f = open("file.txt", "w")
#     f.write("Hello, world!")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     print(f.read())
# finally:
#     # f.close()
#     # print("File is now closed")
#     raise TypeError("I raised this error")


# height = float(input("Height: "))
# weight = float(input("Weight: "))

# if height > 3:
#     raise ValueError("Human height must be under 3 meters")

# bmi = weight / height ** 2
# print(f"BMI: {bmi:.2f}")


fruits = ["Apple", "Pear", "Orange"]

# TODO: Catch the exception and make sure the code runs without crashing.
# TODO: Take Default value as Fruit Pie.


def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")

try:
    make_pie(4)
except IndexError:
    print("Fruit pie")


# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")

# make_pie(4)


facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)
