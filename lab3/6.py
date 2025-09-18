# Program to check whether the number is a palindrome.

num = int(input("Enter a number:"))
original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num = num // 10

if original_num == reversed_num:
    print("Palindrome")
else:
    print("Not a palindrome")