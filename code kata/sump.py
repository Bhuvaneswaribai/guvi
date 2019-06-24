in1,in2,in3=map(int,input().split())
st=0
for i in range(1,in3+1):
 st+=in1+(in3-i)*in2
print(st)
