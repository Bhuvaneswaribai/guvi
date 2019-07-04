from itertools import combinations
Number,K=input().split()
K=int(K)
leng=[]
dd=combinations(Number,len(Number)-K)
for i in list(dd):
  leng.append("".join(i))
print(min(leng))
