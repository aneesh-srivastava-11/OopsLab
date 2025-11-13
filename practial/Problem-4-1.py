def flatten(nested):
  flat=[]
  for i in nested:
   for item in i:
            flat.append(item)
  return flat
print("Sample Input : [[1,2], [3,4,5], [6]]")
nested = [[1,2], [3,4,5], [6]]
print("output:", flatten(nested))

