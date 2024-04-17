# with open("weather-data.csv", "r") as file:
#     data = file.readlines()

# print(data)


# import csv 

# with open("weather-data.csv", "r") as file1:
#     reader = csv.reader(file1)
#     temperatures = []
#     for row in reader:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

'''
import pandas

data = pandas.read_csv("weather-data.csv")
print(data)
print(data["temp"])

print(type(data))#do dataframe operations on it
print(type(data["temp"])) #do series operations on it

# https://pandas.pydata.org/docs/reference/index.html
# https://pandas.pydata.org/docs/

data_dict = data.to_dict()
print(data_dict)

temper = data["temp"]

temp_list = temper.to_list()
print(temp_list)

# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)
#or
avg_temp = temper.mean()
print(avg_temp)

max_temp = temper.max()
#or
# max_temp = max(temp_list)
print(max_temp)

#getting other data from csv
print(data["condition"])
# or
print(data.condition)

#getting row data from csv

# print(data["day"] == "Monday")
print(data[data.day == "Monday"])

print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# print(monday.condition)


monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)

mon_temp_f = (9/5)*monday_temp + 32
print(mon_temp_f)


# Create dataframe from scratch
data_dict = {
    "students": ["Mokshit", "Mohit", "Ketan"],
    "Marks": [99,88,77],
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv") #creates csv file with data
print(data)

'''

'''import pandas 

squirrel_data = pandas.read_csv("Squirrel-Census-Data.csv")

fur_colour = squirrel_data["Primary Fur Color"]
# # fur_list = fur_colour.to_list()
# # print(fur_list)

# cinnamon_fur = squirrel_data[fur_colour == "Cinnamon"].to_dict()
# gray_fur = squirrel_data[fur_colour == "Gray"].to_dict()
# black_fur = squirrel_data[fur_colour == "Black"].to_dict()

# print(cinnamon_fur)

# squirrel_dict = squirrel_data.to_dict()
# print(squirrel_dict)



# fur_colour = squirrel_data["Primary Fur Color"]
fur_list = fur_colour.to_list()
# # print(fur_list)

cinnamon_count = fur_list.count("Cinnamon")
gray_count = fur_list.count("Gray")
black_count = fur_list.count("Black")

# # print(cinnamon_count)
# # print(fur_colour)

# # cinnamon_fur = squirrel_data[fur_colour == "Cinnamon"]
# # gray_fur = squirrel_data[fur_colour == "Gray"]
# # black_fur = squirrel_data[fur_colour == "Black"]

# # print(cinnamon_fur.)

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_count, black_count, cinnamon_count],
}

df = pandas.DataFrame(data_dict)

df.to_csv("Squirrel_count.csv")

'''


