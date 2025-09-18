# Program to convert a nested list to a flat list.

nested = []
n = int(input("Enter number of sublists: "))
for i in range(n):
    sublist_input = input(f"Enter elements of sublist {i+1}: ")
    sublist = [int(val) for val in sublist_input.strip().split()]
    nested.append(sublist)

flat = []
for group in nested:
    for item in group:
        flat.append(item)

print("Flattened list:", flat)