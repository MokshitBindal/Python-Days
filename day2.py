'''str="Hello"
str1=str[0]
print(str1)

print("Hello"[0])
print("123"+"456"[1])
print("123","456",[3])
print(("123"+"456")[3])
print(123+456)
print(123,234_567_895)
print(3.1415)
print(True,False)'''
# len of int gives error

"""num_char = len(input("What is your name? "))
print(type(num_char))
print("your name has " + str(num_char) + " characters.")
#cant add int to string
print("Your name is {} characters long.".format(num_char))"""

'''a=float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70)+str(100))

number=input("Type a 2 digit number. ")
add=int(number[0])+ int(number[1])
print(add)

print(6/3) # gives float
print(7//3) #floor division,gives int
print(2**3) # 2 power 3
print(7%3) # gives remainder
'''
# PEDMAS LR
# ()
# **
# * /
# + -
# calculation goes from left to right


'''weight=int(input("Enter your weight.(in kg) "))
height=float(input("Enter your height.(in m) "))

bmi=weight/height**2

print("your bmi is {}".format(int(bmi)))'''

'''print(round(8/3))

print(round(8/3,2))

result = 4/2
result /= 2
print(result)

score = 0
score += 1

print(score)

height = 1.8
iswinning = True
# f-strings let you add data to print
# without being always changing the data
# from like float to string
print(f"your score is {score}"
      f",your height is {height},are you winning is {iswinning}")'''


'''
your_age = int(input("What is your age right now? "))
age_left = 90-your_age
life_in_day = age_left*365
life_in_weeks = age_left*52
life_in_months = age_left*12

print(f"Your life in days is {life_in_day} / "
      f"Your life in weeks is {life_in_weeks} / "
      f"Your life in months is {life_in_months}.")
'''

total_bill = float(input("What is the total bill amount? $"))
total_people = int(input("How many people are involved? "))
tip = int(input("How much tip you want to give(in %)? "))
actual_bill = total_bill + (total_bill * tip / 100)
actual_bill_per_person = actual_bill / total_people
final_bill = "{:.2f}".format(actual_bill)
final_bill_per_person = "{:.2f}".format(actual_bill_per_person)
# here round would have given 200/5 as 40.0
# even with round set to 2
# and not 40.00
# so we used format so we get exactly 2 decimal places everytime
print(f"Bill amount per person is ${final_bill_per_person}"
      f" for a total amount of ${final_bill} ")
print(type(final_bill))
