n1,v1=map(int,(input().split()))
a1=0
for x1 in range(2,v1):
        if(n1%x1==0 and v1%x1==0):
            a1=x1
print(a1)
