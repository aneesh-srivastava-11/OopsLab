s = input("enter a string")
s1 = ""
for ch in s:
    if ch.isalnum():
        s1 += ch
print("Original:", s)
print("Cleaned:", s1)
