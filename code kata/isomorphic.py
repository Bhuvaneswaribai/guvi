n,n2=map(str,input().split())
if(len(n)!=len(n)):
  print("no")
a=[n.count(i) for i in n]
b=[n2.count(i) for i in n2]
if a==b:
  print("yes")
else:
  print("no")
