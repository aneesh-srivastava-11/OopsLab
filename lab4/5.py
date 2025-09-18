# Program to find the union and intersection of two lists without using sets.

list1 = input("Enter first list:").split()
list2 = input("Enter second list:").split()

a = [int(x) for x in list1]
b = [int(y) for y in list2]

intersection = []
union = []

# Find intersection
for i in a:
    if i in b and i not in intersection:
        intersection.append(i)

# Find union
for i in a:
    if i not in union:
        union.append(i)

for j in b:
    if j not in union:
        union.append(j)

print("Intersection:", intersection)
print("Union:", union)