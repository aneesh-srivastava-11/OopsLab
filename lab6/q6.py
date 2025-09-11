def is_palindrome(n):
    rev = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10
    return n == rev
def largest_palindrome(start, end):
    for num in range(end, start - 1, -1):
        if is_palindrome(num):
            return num
    return 
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
result = largest_palindrome(start, end)
if result:
    print("Largest palindrome in range:", result)
else:
    print("No palindrome found in the given range.")