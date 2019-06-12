n, b = input().split() 
n = int(n)
b = int(b)
for num in range(n+1,b, 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
  
