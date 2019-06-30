n1=list(map(int,input().split()))
nn2=list(map(int,input().split()))
for k in range(0,n1[1]):
  nn2=[nn2[-1]] + nn2[:-1]
print(*nn2,end=' ')
