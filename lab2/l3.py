#greatest number of all
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(a, "is the greatest")
elif b >= a and b >= c:
    print(b, "is the greatest")
else:
    print(c, "is the greatest")
6