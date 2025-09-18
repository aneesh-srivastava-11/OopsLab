# Program to reverse a number or string.

user_input = input("Enter a number or string:")

if user_input.isdigit():
    num = int(user_input)
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num = num // 10
    print(f"The reversed number is: {reversed_num}")
else:
    # This section handles strings, although the handwritten code only shows the number logic.
    reversed_string = user_input[::-1]
    print(f"The reversed string is: {reversed_string}")