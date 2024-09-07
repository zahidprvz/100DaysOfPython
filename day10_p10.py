# def is_leap(given_year):
#     if given_year % 4 == 0:
#         if given_year % 100 == 0:
#             if given_year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
# # Actual code to implement logic
#
# def days_in_month(is_leap_year, asked_month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if asked_month == 2 and is_leap_year:
#         return 29
#     else:
#         return month_days[asked_month - 1]
#
# # Main program running entry point
#
# year = int(input("Enter the year: "))
# month = int(input("Enter the month: "))
# days = days_in_month(is_leap(year), month)
#
# print(days)

# Calculator

# Add operation
def add(n1, n2):
    return n1 + n2

# Subtract operation
def subtract(n1, n2):
    return n1 - n2

# Divide operation
def divide(n1, n2):
    return n1 / n2

# Multiply operation
def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

def calculator():
    # print(logo)
    num1 = float(input("Enter the first number? "))
    for op in operations:
        print(op)
    should_continue = True
    while should_continue:
        op_symbol = input("Pick an operation: ")
        num2 = float(input("Enter the next number? "))

        calculate_function = operations[op_symbol]
        answer = calculate_function(num1, num2)

        print(f"{num1} {op_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()