    
g=int(input())
s=list(str(g))
for i in range(0, len(s)): 
  s[i] = int(s[i])
v=0
for i in range(0,len(s)):
  v=s[i]**3+v
if(v==g):
  print("yes")
else:
  print("no")
