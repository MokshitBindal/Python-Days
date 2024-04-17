'''height = int(input("What is your height in cm? "))
if height >= 120:
    print("Enjoy the ride")
else:
    print("Sorry but you can't ride the rollercoaster. ")'''

'''
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
'''

'''
height = int(input("What is your height in cm? "))
if height >= 120:
    print("Enjoy the ride")
    age = int(input("What is your age? "))
    if age == 18:
        print("Please pay 100rs.")
    elif age > 18:
        print("Please pay 150 rs.")
    else:
        print("Please pay 50rs.")
else:
    print("Sorry but you can't ride the rollercoaster.")
'''

'''
weight=int(input("Enter your weight.(in kg) "))
height=float(input("Enter your height.(in m) "))
bmi=round(weight/height**2,2)
if bmi < 18.5:
    print("your bmi is {},you are underweight".format(bmi))
elif bmi <25:
    print("your bmi is {},you are normal weight".format(bmi))
elif bmi < 30:
    print("your bmi is {},you are overweight".format(bmi))
elif bmi <35:
    print("your bmi is {},you are obese".format(bmi))
else:
    print("your bmi is {},you are clinically obese".format(bmi))
'''

'''year = int(input("Write any year. "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year.")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")'''


def leap_year_finder(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


'''
print("        Welcome to the 29,FEB age calculator.     ")
age = 0
birthyear = int(input("In which leap year you were born? "))
if leap_year_finder(birthyear) == True:
    for i in range(birthyear+1,2023):
        if leap_year_finder(i) == True:
            age += 1
else:
    print("give a leap year as input.")
print(age)
'''

'''
if year % 4 == 0:
    if year % 100 = 0:
        if year % 400 == 0:
            print(f"The year {year} is a leap year.")
        else:
            print("the year {} is not a leap year.".format(year))
    else:
        print("the year {} is a leap year.".format(year))
else:
    print("the year {} is not a leap year.".format(year))
'''

height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("Enjoy the ride")
    age = int(input("What is your age? "))
    if age == 18:
        bill = 100
        # print("Please pay {}rs.".format(bill))
    elif age > 18 and age < 45:
        bill = 150
        # print("Please pay {}rs.".format(bill))
    elif age >= 45 and age <= 55:
        print("Have a free ticket for ride from us")
    else:
        bill = 50
        # print("Please pay {}rs.".format(bill))

    photo = input("Do you want a photo? Y or N: ")
    if photo == "y" or "Y":
        bill += 50
    print(f"Please pay {bill}rs")

else:
    print("Sorry but you can't ride the rollercoaster.")

'''    
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want extra pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size in ["s", "S"]:
    bill = 150
elif size in ["m", "M"]:
    bill = 200
else:
    bill = 250

if add_pepperoni in ["y", "Y"]:
    if size in ["s", "S"]:
        bill += 10
    else:
        bill += 30

if extra_cheese in ["y", "Y"]:
    bill += 10

print(f"Your total bill is {bill}rs")
'''

# a = 12
# print(a < 15)
# print(a > 10)
# print(a > 10 and a < 15)
# print(a>15)
# print(a>10 or a>15)
# print(not a>15)
