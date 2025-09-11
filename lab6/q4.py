def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
count=int(input("how many numbers of terms you want"))
print("Fibonacci series using recursion:")
for i in range(count+1):
    print(fibonacci(i), end=" ")