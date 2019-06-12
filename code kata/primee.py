n, b = input().split() 
n = int(n)
b = int(b)
for nu in range(n+1,b, 1):
   if nu > 1:
       for i in range(2,nu):
           if (nu % i) == 0:
               break
       else:
           print(num)
  
