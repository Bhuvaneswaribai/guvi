n=int(input())
te=n
re=0
while(n>0):
    dig=n%10
    re=re*10+dig
    n=n//10
if(te==re):
    print("yes")
else:
    print("no")
