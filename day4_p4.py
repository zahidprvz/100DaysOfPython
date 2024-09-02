# # # import random
#
# # # # rand_int = random.randint(1, 6)
# # # # print(rand_int)
#
# # # rand_int = random.randint(0, 1)
#
# # # if rand_int == 0:
# # #     print("Heads")
# # # else:
# # #     print("Tails")
#
# # names = ["zahid", "namal", "ali", "zulfiqar", "umair", "wahab"]
#
# # import random
#
# # length = len(names)
# # chosen_index = random.randint(0, length - 1)
# # person = names[chosen_index]
# # print(f"{person} will pay the bill")
#
# line1 = [" ", " ", " "]
# line2 = [" ", " ", " "]
# line3 = [" ", " ", " "]
#
# map = [line1, line2, line3]
#
# print("\nHiding  your treasure! X marks the spot!\n")
#
# position = input("Where do you want to put the treasure? ")
# letter = position[0].lower()
# abc = ["a", "b", "c"]
#
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
#
# map[number_index][letter_index] = "X"
#
# print(f"{line1}\n{line2}\n{line3}")


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

# Get user's choice
try:
    user_choice = int(input("What do you choose? type 0 for rock, 1 for paper and 2 for scissors: "))
    if user_choice < 0 or user_choice > 2:
        raise ValueError("Invalid choice")

    print("You chose:")
    print(choices[user_choice])

    # Generate computer's choice
    rand_choice = random.randint(0, 2)
    print("Computer chose:")
    print(choices[rand_choice])

    # Determine the winner
    if user_choice == rand_choice:
        print("It's a draw!")
    elif (user_choice == 0 and rand_choice == 2) or \
         (user_choice == 1 and rand_choice == 0) or \
         (user_choice == 2 and rand_choice == 1):
        print("You win!")
    else:
        print("You lose!")

except ValueError as e:
    print(e)
