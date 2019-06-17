    
s=input()
leter = False
numer = False
for l in s:
  if l.isalpha():
      leter = True
  if l.isdigit():
      numer = True
if leter and numer:
      print('Yes')
else:
  print('No')
