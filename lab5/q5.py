input_str=input("enter tuple values : ").split()
lst=[]
for x in input_str:
  lst.append(int(x))
index=int(input("enter index to modify: "))
new_val=int(input("enter new value"))
lst[index]=new_val
t=tuple(lst)
print("Modified tuple :",t)