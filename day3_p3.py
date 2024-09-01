# # # # # # # # number = int(input("Enter your number: "))

# # # # # # # # if number % 2 == 0:
# # # # # # # #     print(f"{number} is even!")
# # # # # # # # else: 
# # # # # # # #     print(f"{number} is odd!")

# # print("*****Welcome to the Roller Coaster Ticket Counter*****\n\n")

# # height = int(input("What is your height in (cm) : "))
# # bill = 0

# # if height >= 120:
# #     age = int(input("What is your age (years) : "))
# #     if age < 12:
# #         bill = 5
# #         print("Child's ticket price is 5$")
# #     elif age <= 18:
# #         bill = 7
# #         print("Teen's ticket price is 7$")
# #     elif age > 18 and age < 45:
# #         bill = 12
# #         print("Adult's ticket price is 12$")
# #     elif age >= 45 and age <= 55:
# #         bill = 0
# #         print("People with age 45 - 55 can ride for free!")

# #     extra_photo = input("Do you want an extra photo for 3$? ( 'Y' or 'N') ")
# #     if extra_photo == 'Y':
# #         bill += 3
# #         print(f"Your total bill is: {bill}")
# #     else:
# #         print(f"Your total bill is: {bill}")
# # else:
# #     print("Sorry, you have to grow taller before you can ride!")

# # # # # # print("*****Welcome to the BMI calculator!*****")

# # # # # # height = float(input("Enter your height (meters) : "))
# # # # # # weight = float(input("Enter your weight (kg) : "))

# # # # # # bmi = weight / (height ** 2)

# # # # # # rounded_bmi = round(bmi, 2)

# # # # # # if rounded_bmi < 18:
# # # # # #     print(f"Your bmi is {rounded_bmi}, you are underweight!")
# # # # # # elif rounded_bmi < 25:
# # # # # #     print(f"Your bmi is {rounded_bmi}, you have a normal weight!")
# # # # # # elif rounded_bmi < 30:
# # # # # #     print(f"Your bmi is {rounded_bmi}, you are slightly overweight!")
# # # # # # elif rounded_bmi < 35:
# # # # # #     print(f"Your bmi is {rounded_bmi}, you are obese!")
# # # # # # else:
# # # # # #     print(f"Your bmi is {rounded_bmi}, you are clinically obese!")

# # # # # print("*****Welcome to the Leap Year Checker*****\n\n")

# # # # # year = int(input("Enter the year: "))

# # # # # if year % 4 == 0:
# # # # #     if year % 100 == 0:
# # # # #         if year % 400 == 0:
# # # # #             print("It's a leap year!")
# # # # #         else:
# # # # #             print("It's not a leap year!")
# # # # #     else:
# # # # #         print("It's a leap year!")
# # # # # else:
# # # # #     print("It's not a leap year!")

# # # print("Welcome to the Python Pizza Delivery Service!")

# # # # small pizza 15$
# # # # medium pizza 20$
# # # # large pizza 25$

# # # size = input("Do you want small (S) / large (L) / medium (M) size? ")
# # # add_pepperoni = input("Do you want pepperoni or not? 'Y' or 'N' : ")
# # # add_extra_cheese = input("Do you want extra cheese ? 'Y' or 'N' : ")

# # # pizza_price = 0
# # # s_pizza = 15
# # # m_pizza = 20
# # # l_pizza = 25
# # # extra_pepp_small = 2
# # # extra_pepp_med_or_large = 3
# # # extra_cheese = 1

# # # if size == 'S':
# # #     if add_pepperoni == 'Y':
# # #         if add_extra_cheese == 'Y':
# # #             pizza_price = s_pizza + extra_pepp_small + extra_cheese
# # #         else:
# # #             pizza_price = s_pizza + extra_pepp_small
# # #     else:
# # #         pizza_price = s_pizza
# # # elif size == 'M':
# # #     if add_pepperoni == 'Y':
# # #         if add_extra_cheese == 'Y':
# # #             pizza_price = m_pizza + extra_pepp_med_or_large + extra_cheese
# # #         else:
# # #             pizza_price = m_pizza + extra_pepp_med_or_large
# # #     else:
# # #         pizza_price = m_pizza  
# # # elif size == 'L':
# # #     if add_pepperoni == 'Y':
# # #         if add_extra_cheese == 'Y':
# # #             pizza_price = l_pizza + extra_pepp_med_or_large + extra_cheese
# # #         else:
# # #             pizza_price = l_pizza + extra_pepp_med_or_large
# # #     else:
# # #         pizza_price = l_pizza

# # # print(f"Your total bill for the pizza is: {pizza_price}")


# print("Welcome to the Love Calculator!\n\n")

# first_name = input("What is your name: ")
# second_name = input("What is partner's name: ")

# combined_names = first_name + second_name
# lower_names = combined_names.lower()

# t = lower_names.count('t')
# r = lower_names.count('r')
# u = lower_names.count('u')
# e = lower_names.count('e')

# first_digit = t + r + u + e

# l = lower_names.count('l')
# o = lower_names.count('o')
# v = lower_names.count('v')
# e = lower_names.count('e')

# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))
 
# if score < 10 or score > 90:
#     print(f"Your score is {score}, you go togther like coke & mentos!")
# elif score >= 40 and score <= 50:
#     print(f"Your score is {score}, you alright together!")
# else:
#     print(f"Your score is {score}")

print("Welcome to the Treasure Hunt Game!")

choice_1 = (input("Welcome to th Treasure Island. Your mission is to find treasure.\nPress yes or no: ")).lower()

if choice_1 == 'yes':
    choice_2 = (input("\nYou have to choose one road | move left or right? ")).lower()
    if choice_2 == 'right':
        print("\nThere was a khayi ahead, \nYou fell and Game over!")
    else:
        choice_3 = (input("\nYou continued the road but then came a lake, type 'swim' to or 'continue' to continue on the road? ")).lower()
        if choice_3 == 'swim':
            print("\nyou swam and reached to the treasure. \nCongratulations! You won.")
        else:
            choice_4 = (input("\nYou continue to the road, and came across a tunnel, type 'left' or 'right' to move in direction: ")).lower()
            if choice_4 == 'right':
                print("\nYou chose the right path and found the treasure!\nCongratulations! You won.")
            else:
                print("\nYou chose the wrong path!!\nGame Over")


else:
    print("\nGame over!")