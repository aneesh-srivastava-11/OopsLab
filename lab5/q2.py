text = input("Enter main string: ")
sub = input("Enter substring to search: ")
count = 0
i=0
while i<=len(text)-len(sub):
    if text[i:i+len(sub)] == sub:
        count += 1
    i+=1
print("Count of substring:", count)
