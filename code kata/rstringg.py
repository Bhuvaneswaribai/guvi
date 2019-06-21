ab=int(input())
ab=str(ab)
f=0
for i in range(0,len(ab)):
  if(ab[i]=='0' or ab[i]=='1'):
    f=1
  else:
    f=0
    break
if(f==1):
  print("yes")
else:
  print("no")
