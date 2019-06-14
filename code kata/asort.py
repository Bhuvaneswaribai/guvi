bi = int(input())
a = list(map(int,input().split()))
a.sort()
for i in range(0,bi):
   print(a[i],end=" ")
