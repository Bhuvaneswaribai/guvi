    
n1=int(input())
se=0
while(n1!=0):
  a=n1%10
  se=se+(a*a)
  n1=n1//10
print(se)
