'''
print("Welcome To The Band Name Generator")

city = input("What is the name of the city you live in?\n")

animal = input("what is the name of your favourite animal/insect?\n")

print("The name of your band could be " + city + " " + animal)

print("{} {}".format(city,animal))
'''

# print("Hello World!")
#
# print("day1- programming\nprint\n function")
# print("the function will work like this")
# print('print("how to print")')
#
#
# print("Hello " + input("What is your name?") + "!")

'''name = input("What is your name? ")
print(len(name))
'''
# print(len(input("What is your name? ")))


'''a = input("a = ")
b = input("b = ")
c = a
a = b
b = c
print("now a =",a)
print("now b =",b)
'''

'''
def fibonacci_series(n):
    if n < 0:
        print("wrong input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)

print(fibonacci_series(9))'''

'''
n1 = 0
n2 = 1
nterms = int(input("how many fibonacci series numbers: "))
for i in range(nterms):
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
'''

'''
num = int(input("write a number to check for prime"))

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(f"{num} isn't prime")
            break
    else:
        print("prime number")
'''

# program to find all prime b/w 1 and 50
'''
for j in range(1,51):
    for i in range(2,j):
        if j % i == 0:
            break
    else:
        print(f"{j} is a prime number")
'''