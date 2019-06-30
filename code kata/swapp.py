mas=input()
l=[mas[i] for i in range(len(mas)) if i%2==0]
l1=[mas[i] for i in range(len(mas)) if i%2!=0]
for j in range(len(mas)//2):
  print(l1[j]+l[j],end="")
