h,j=map(int,input().split())
for f in range(h+1,j):
    w=len(str(f))
    h=str(f)
    l=list(map(int,h))
    li=[i**w for i in l]
    k=sum(li)
    if(k==f):
        print(k,end=' ')
