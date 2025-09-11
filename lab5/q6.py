tuples=[(1,4),(2,1),(3,3)]
n=len(tuples)
for i in range(n):
  for j in range(0,n-i-1):
    if(tuples[j][1]>tuples[j+1][1]):
      tuples[j],tuples[j+1]=tuples[j+1],tuples[j]
print("sorted list by second element : ",tuples)