    
in1,in2=map(int,input().split())
au=list(map(int,input().split()))
b=[]
for i in range(0,len(au)):
	if(au[i]%2!=0):
		b.append(au[i])
print(b[in2-1])
