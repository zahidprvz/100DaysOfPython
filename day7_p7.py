print(r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
''')

hangman = [r''' 
____
|/   |
|   
|    
|    
|    
|
|_____
''',
           r'''
            ____
           |/   |
           |   (_)
           |    
           |    
           |    
           |
           |_____
           ''',
           r'''
            ____
           |/   |
           |   (_)
           |    |
           |    |    
           |    
           |
           |_____
           ''',
           r'''
            ____
           |/   |
           |   (_)
           |   \|
           |    |
           |    
           |
           |_____
           ''',
           r'''
            ____
           |/   |
           |   (_)
           |   \|/
           |    |
           |    
           |
           |_____
           ''',
           r'''
            ____
           |/   |
           |   (_)
           |   \|/
           |    |
           |   / 
           |
           |_____
           ''',
           r'''
            ____
           |/   |
           |   (_)
           |   \|/
           |    |
           |   / \
           |
           |_____
           ''',
           r'''
            ____
           |/   |
           |   (_)
           |   /|\
           |    |
           |   / \
           |
           |_____
           ''']

from random_word import RandomWords

r = RandomWords()

# Generating a random word
random_word_string = r.get_random_word()
# print(f"Random word: {random_word_string}")

# Converting random word string to list
random_word_list = list(random_word_string)

chances = len(hangman)

# Initialize dash_string_list with underscores
dash_string_list = ["_" for _ in range(len(random_word_string))]

print(f"There are {len(dash_string_list)} characters in the word.\n")
print(' '.join(dash_string_list))

user_string_list = []

while chances > 0 and "_" in dash_string_list:
    user_input = input("\nEnter your character to make the guess: ").lower()

    # Input validation
    if len(user_input) != 1 or not user_input.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    # Check if the letter has already been guessed
    if user_input in user_string_list:
        print("You already guessed that letter!")
        continue

    user_string_list.append(user_input)

    # Check if the guess is correct
    if user_input in random_word_list:
        for index, letter in enumerate(random_word_list):
            if letter == user_input:
                dash_string_list[index] = user_input
        print("Good guess!")
    else:
        chances -= 1
        print("Wrong guess!")

    # Print current state
    print(f"Current word: {' '.join(dash_string_list)}")
    print(f"Remaining chances: {chances}")
    print(hangman[len(hangman) - chances - 1])

# End of game
if "_" not in dash_string_list:
    print("Congratulations! You've guessed the word!")
else:
    print(f"Game over! The word was: {random_word_string}")
print(hangman[len(hangman) - 1])
