ae = input()
b = ["a","e","i","o","u","A","E","I","O","U"]
c=len(ae)
for i in range(0,c):
  if(ae[i] in b):
    print("yes")
    break
else:
  print("no")
