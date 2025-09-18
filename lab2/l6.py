#lowercase
ch = input("Enter a character: ")

if ch.isupper():
    print(ch, "is Uppercase")
elif ch.islower():
    print(ch, "is Lowercase")
elif ch.isdigit():
    print(ch, "is Digit")
else:
    print(ch, "is Special Symbol")
