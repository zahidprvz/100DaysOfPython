# # # two_digit_number = input("Enter two digit number: ")

# # # first_digit = int(two_digit_number[0])
# # # second_digit = int(two_digit_number[1])

# # # result = first_digit + second_digit

# # # print(result)

# # # print(3 * (3 + 3) / 3 - 3)

# # print("Welcome to BMI calculator!")

# # height = input("Enter your height (meters) : ")
# # weight = input("Enter your weight (kg) : ")

# # weight_as_int = int(weight)
# # height_as_float = float(height)

# # bmi = weight_as_int / (height_as_float ** 2)

# # print("Nomral BMI is between 18 - 25!\n Your BMI is: " + str(int(bmi)))

# age = input("Enter your age: ")
# years = 90 - int(age)

# weaks = years * 52

# print(f"You have {weaks} weaks left in your life!")

print("**********Welcome to the Tip Calculator**********\n\n")

total_bill = input("What is your total bill?")
total_members = input("How many members to split bill?")
tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")

total_bill_as_float = float(total_bill)
total_members_as_float = float(total_members)
tip_percentage_as_float = int(tip_percentage)

each_person_pay = (total_bill_as_float / total_members_as_float) * float(f"1.{tip_percentage_as_float}")
final_amount = "{:.2f}".format(each_person_pay)
print(f"Each person should pay ${final_amount}")
