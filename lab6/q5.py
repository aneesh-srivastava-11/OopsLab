
n = int(input("Enter a number: "))
def is_harshad(num):
 s = 0
 temp = n
 while temp > 0:
       d = temp % 10
       s = s + d
       temp = temp // 10
 return n%s==0
if is_harshad(n):
    print("Harshad number")
else:
    print("Not a Harshad number")