    
tp=int(input())
w=[(k) for k in input().split()]
for m in range(0,tp):
  if(w.count(w[m])==1):
    print(w[m])
