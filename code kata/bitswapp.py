u,k=map(int,input().split())
u = u ^ k
k = u ^ k
u = u ^ k
print(u,k)
