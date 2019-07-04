pr,q=map(int,input().split())
input()
w=list(map(int,input().split()))
v=list(map(int,input().split()))
for a in v:
    w.append(a)
    print(max(w),end=' ')
