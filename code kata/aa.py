n1=[]
n2=int(input())
n3=input().split()
for i in n3:
  n1.append(i)
n1.sort()
n1.sort(key=len)
for i in n1:
  print (i,end=' ')
