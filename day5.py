# fruits = ["apples", "banana", "peaches"]

# for fruit in fruits:
#     print(fruit)


'''
student_heights = input("Please enter the heights of students separated by space: ").split()
total = 0
students = 0
for n in student_heights:
    students += 1
for i in student_heights:
    total += int(i)

print(round(total/students))
'''


'''
hey = [134,2456,2,46,3,5,6,3,2,5643,2,5,6666,3245]
print(sum(hey))'''
# adds all items in list

'''
student_scores = input("Please give the scores separated by comma ").split(",")
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

'''

'''
max = 0
for i in range(0 ,len(student_scores)-1):
    if max > student_scores[i+1]:
        max = max
    elif student_scores[i] > student_scores[i+1]:
        max = student_scores[i]
    else:
        max = student_scores[i+1]

print(max)
'''

'''
max = 0
for score in student_scores:
    if score > max:
        max = score
print(max)
'''

# [78,56,89,81,98,67,52,77]

'''
num = 0
for i in range(1,101):
    num += i
print(num)

even = 0
for i in range(2,101,2):
   # if i % 2 == 0:
    even += i
print(even)

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
'''

'''
import random
pass_length = int(input("How long should be the generated password: "))
password = ""
for i in range(pass_length):
    pass_letters = random.choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,./;'[]=-987654321!@#$%^&*()_+{}:")
    password += pass_letters

print(password)
'''

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


# easy level : a random password,not completely, position of letters and numbers can be same
'''
password = ""

for i in range(nr_letters):
    pass_letters = random.choice(letters)
    password += pass_letters

for i in range(nr_symbols):
    pass_symbols = random.choice(symbols)
    password += pass_symbols

for i in range(nr_numbers):
    pass_numbers = random.choice(numbers)
    password += pass_numbers

'''

# hard level : complete random password
'''
passlist = []
total = nr_symbols + nr_numbers + nr_letters
for i in range(nr_letters):
    pass_letters = random.choice(letters)
    passlist.append(pass_letters)

for i in range(nr_symbols):
    pass_symbols = random.choice(symbols)
    passlist.append(pass_symbols)

for i in range(nr_numbers):
    pass_numbers = random.choice(numbers)
  #  passlist += pass_numbers
    passlist.append(pass_numbers)

random.shuffle(passlist)
password = ""
for p in passlist:
    password += p

print(password)
'''


#Another way
'''
access = 0
j = 0
k = 0
l = 0
password = ""
total = nr_symbols + nr_numbers + nr_letters
while len(password) != total:
    choice = random.randint(1,3)

    if choice == 1:
        access = nr_letters
        if access != j:
            pass_letters = random.choice(letters)
            password += pass_letters
            j += 1
            
    elif choice == 2:
        access = nr_symbols
        if access != k:
            pass_symbols = random.choice(symbols)
            password += pass_symbols
            k += 1

    elif choice == 3:
        access = nr_numbers
        if access != l:
            pass_numbers = random.choice(numbers)
            password += pass_numbers
            l += 1
print(password)
'''