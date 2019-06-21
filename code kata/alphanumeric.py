l1u=input()
v=[]
for i in l1u:
  if(i.isnumeric()):
    v.append(i)
print(*v,sep='')
