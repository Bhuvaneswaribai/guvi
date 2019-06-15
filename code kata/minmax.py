n = int(input())
h =[]
for i in range(n):
 h = list(map(int,input().split())) 
 print(min(h),max(h),end = ' ') 
