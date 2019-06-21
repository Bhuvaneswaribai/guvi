pqa=int(input())
if pqa>0:
  for x in range(2,pqa):
    if(pqa%x==0):
      print("yes")
      break
  else:
    print("no")
else:
  print("yes")
