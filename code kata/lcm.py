import math
z,z2=input().split()
z=int(z)
z2=int(z2)
z3=(math.gcd(z,z2))
print((z*z2)//z3)
