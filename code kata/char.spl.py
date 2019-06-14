u=input()
y=0
for i in range(len(u)):
  if(u[i].isdigit() or u[i].isalpha() or u[i]==' '):
    continue
  else:
    y=y+1  
print(y)
