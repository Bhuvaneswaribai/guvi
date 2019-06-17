i,j=map(int,input().split())
mk=list(input().split())
counit=0
if(len(mk)==i):
  for n in mk:
    if(int(n)==j):
      counit=counit+1
  print(counit)
