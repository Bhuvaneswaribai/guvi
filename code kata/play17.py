import math
xd,y=list(map(int,input().split()))
s=math.gcd(xd,y)
print((xd*y)//s)
