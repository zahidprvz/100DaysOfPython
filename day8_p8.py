#
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#
# def caesar(given_text, shift_amount, task):
#     if task == "encode":
#         plain_text = ""
#
#         for letter in given_text:
#             position = alphabet.index(letter)
#             new_position = position + shift_amount
#             new_letter = alphabet[new_position]
#             plain_text += new_letter
#         print(f"The encoded text is: {plain_text}")
#     elif task == "decode":
#         plain_text = ""
#
#         for letter in given_text:
#             position = alphabet.index(letter)
#             new_position = position - shift_amount
#             new_letter = alphabet[new_position]
#             plain_text += new_letter
#         print(f"The decoded text is: {plain_text}")
#
#     else:
#         print("You wrote invalid command!")
#
#
# caesar(text, shift_amount=shift,task=direction)
