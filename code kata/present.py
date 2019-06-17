ii,j=map(int,input().split())
kk=list(input().split())
count=0
if(len(kk)==ii):
  for n in kk:
    if(int(n)==j):
      count=1
  if(count==1):
    print("yes")
  else:
    print("no")
