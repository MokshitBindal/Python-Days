'''file1 = open("PythonDays/day24/myfile.txt", 'r')
contents = file1.read()
print(contents)
file1.close()
'''
# print("\033c")

filepath = "myfile.txt"
new_path = "/home/Mokshit/newfile.txt"

with open(filepath) as f:
    contents = f.read()
    print(contents)

with open(filepath, mode="w") as f:
    #write mode creates file if it doesn't exist
    f.write("I am not interested, bye.")
    # clears everything and write the line

with open(filepath, mode="a") as f:
    f.write("New line mate")
    #appends after text, not in new line
    f.write("\nThis is how you write in new line")

with open(new_path) as f:
    contents = f.read()
    print(contents)

with open("../../../../../Documents/Programming_files/Python/PythonDays/day24/myfile.txt") as f:
    contents = f.read()
    print(contents)

# import os

# filename = './myfile.txt'
# # filename = "PythonDays/day24/myfile.txt"

# if os.path.isfile(filename):
#   print('The file exists.')
# else:
#   print('The file does not exist.')
    




# PLACEHOLDER = "[name]"


# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()

# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)
