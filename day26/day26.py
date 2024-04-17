# numbers = [1,2,3,4,5,6,7]
# num_1 = [n+1 for n in numbers]
# print(num_1)

# name = "Mokshit"
# letters = [letter for letter in name]
# print(letters)

# num_2 = [num*2 for num in range(1,5)]
# print(num_2)

# num_3 = [num for num in range(1,10) if num%2 == 0]
# print(num_3)

# names = ["mokshit", "mohit", "ketan", "deepanshu", "anant", "himanshu"]
# short_names = [name for name in names if len(name) <= 5]
# print(short_names)

# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆

# # Write your 1 line code 👇 below:
# squared_numbers = [num**2 for num in numbers]

# # Write your code 👆 above:

# print(squared_numbers)


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above

# # Write your 1 line code 👇 below:

# result = [num for num in numbers if num % 2 == 0]
# # Write your code 👆 above:

# print(result)


# with open("file1.txt", 'r') as f1:
#     c1 = f1.readlines()
# with open("file2.txt", 'r') as f2:
#     c2 = f2.readlines()

# l1 = [int(item) for item in c1]
# l2 = [int(item) for item in c2]

# # print(c1, c2)
# # print(l1, l2)

# '''result = []
# for item in l1:
#     if item in l2:
#         result.append(item)'''
# result = [item for item in l1 if item in l2]

# # Write your code above 👆

# print(result)

# new_dict = {new_key: new_value for item in list}

# new_dict = {new_key: new_value for (key, value) in dict.items()}


# import random

# names = ["mokshit", "mohit", "ketan", "deepanshu", "anant", "himanshu"]

# student_scores = {student: random.randint(1, 100) for student in names}
# print(student_scores)

# passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
# word_list = sentence.split(" ")
# # print(word_list)
# result = {word:len(word) for word in word_list}
# # Write your code below:


# print(result)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
# weather_f = {day:round(c*(9/5) + 32, 1) for (day,c) in weather_c.items()}

# # Write your code 👇 below:


# print(weather_f)


# import pandas
# student_dict = {
#     "student": ["mokshit", "mohit", "ketan"],
#     "score": [56, 75, 97]
# }

# # for key, value in student_dict.items():
# #     print(key)
# #     print(value)

# student_dataframe = pandas.DataFrame(student_dict)
# # print(student_dataframe)

# # for key, value in student_dataframe.items():
# #     print(key)
# #     print(value)

# for (index,row) in student_dataframe.iterrows():
#     # print(index)
#     # print(row)
#     # print(row.student)
#     # print(row.score)
#     if row.student == "mokshit":
#         print(row.score)

