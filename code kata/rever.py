a=int(input())
bb=0
while(a>0):
  c=a%10
  bb=bb*10+c
  a=a//10
print(bb)
