def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10          
        reversed_num = reversed_num * 10 + digit  
        n = n // 10
    return reversed_num
def reverse_string(s):
    return s[::-1]
str_input = input("Enter a string: ")
print("Reversed string:", reverse_string(str_input))
num = int(input("Enter a positive number: "))
print("Reversed number:", reverse_number(num))