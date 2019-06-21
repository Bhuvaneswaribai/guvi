ss=input()
t=""
for a in ss:
  if a not in t:
    t=t+a
if(ss==t):
  print("Yes")
else:
  print("No")
