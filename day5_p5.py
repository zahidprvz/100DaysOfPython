# # # # students = ["156", "178", "165", "171", "187"]
# # # #
# # # # total_height = 0
# # # # counter = 0
# # # #
# # # # for student in students:
# # # #     total_height += int(student)
# # # #     counter = counter + 1
# # # #
# # # # print(counter)
# # # #
# # # # average = round((total_height / counter), 2)
# # # #
# # # # print(f"Total Height: {total_height} \n Number of students: {counter} \n Average: {average}")
# # #
# # # students = ["156", "178", "165", "171", "187"]
# # # counter = 0
# # # maxElement = 0
# # #
# # # for student in students:
# # #     if int(student) > maxElement:
# # #        maxElement = int(students[counter])
# # #        counter = counter + 1
# # #
# # # print(f"Maximum element in array is: {maxElement}")
# #
# # input_number = int(input("Enter the number till you want the sum? "))
# # sum = 0
# #
# # for num in range(0, input_number + 1, 2):
# #     sum += num
# #
# # print(f"Sum is: {sum}")
#
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

#Password Generator Project


import random
import string

print("Welcome to the PyPassword Generator!")

# Get user input
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Define character sets
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# Generate the password
password = []

# Append random letters
for _ in range(nr_letters):
    password.append(random.choice(letters))

# Append random symbols
for _ in range(nr_symbols):
    password.append(random.choice(symbols))

# Append random numbers
for _ in range(nr_numbers):
    password.append(random.choice(numbers))

# Shuffle the password list to randomize the order
random.shuffle(password)

# Join the list into a string
result = ''.join(password)

print(f"Your random password is: {result}")
