    
n1y=int(input())
n2=0
n3=[]
for i in range(n1):
  n3.append(input())
for i in range(n1y):
  if(sorted(n3[i])==sorted('kabali')):
    n2=n2+1
print(n2)
