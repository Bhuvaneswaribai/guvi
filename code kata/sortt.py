bi = int(input())
ar = list(map(int,input().split()))
ar.sort()
for i in range(0,bi):
   print(ar[i],end=" ")
