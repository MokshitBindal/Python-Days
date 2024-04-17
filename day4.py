'''import random
import my_module #just create a new file and save it,it will work as module when you import it

random_number_int = random.randint(1,10)
# randint includes 1 and 10 as well
print(random_number_int)

random_number_range = random.randrange(1,10)
# randrange doesnt include 10
print(random_number_range)

print(my_module.pi)

random_number_float = random.random()
# inludes all float b/w 0 and 1 but not 1
print(random_number_float)

random_num = random.randint(0,4) + random.random()
# random floating number b/w 0 and 5
print(random_num)


# heads or tails
toss_number = random.randint(0,1)
if toss_number == 0:
    print("Heads")
else:
    print("Tails")

'''

'''
fruits = ["apple", "cherry", "Banana"]
fruits[1] = "orange"
print(fruits[1])
print(fruits[0])
# 0 is the index
print(fruits[-1])

fruits.append("kiwi")
print(fruits)
fruits.extend("kiwi")
print(fruits)
fruits.insert(2, "papaya")
print(fruits)
fruits.remove("kiwi")
print(fruits)
fruits.pop(6)
print(fruits)
print(fruits.index("k"))
a = fruits.copy()
print(a)

fruits.reverse()
#reverse the order in list
num1 = [10,20,50,23,56,98,78,31,45]
num1.sort()
print(num1)
num1.sort(reverse=True)
print(num1)
#sorts the list
# Return a shallow copy of the list
#gives index of k
fruits.clear()
# Remove all items from the list. Equivalent to del a[:].
# pop removes the item at index 6,no index makes it remove the last element
# removes the first kiwi it sees
# adds papaya at index 2
# append adds item wheres extend take a iterable and adds it

print(fruits)

'''
'''
import random
names_string = input("Give me everybody\'s name, separated by comma. ")
names = names_string.split(", ")
print(names)
bill_payer = random.choice(names)
print(f"{bill_payer} will pay the bill today.")

fruit = ["Strawberries",
"Spinach",
"Kale",
"Nectarines",
"Apples",
"Grapes",
"Peaches",
"Cherries"]

vegetables = ["Pears",
"Tomatoes",
"Celery",
"Potatoes"]

dirty_dozen = [fruit,vegetables] # nested list

print(dirty_dozen)
'''

'''
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? \ntop to down: column and left to right: row\n")
map[int(position[1])-1][int(position[0])-1] = "X"
print(map[0])
print(map[1])
print(map[2])
'''
