# Program to swap two numbers without a third variable
a = 5
b = 6
a, b = b, a  # This simultaneously assigns the old value of b to a, and the old value of a to b
print(a)
print(b)