from collections import Counter
f=int(input())
z=list(map(int,input().split()))
x=Counter(z)
list=[]
for i in x.item():
   if(i[1]!=1):
      print(i[0],end="")
for j in x.item():
   list.append(j[1])
if(max(list)==1):
  print("unique")
   
