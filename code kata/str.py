    
sst=list(input())
if len(sst)%2==0:
    sst[int(len(sst)/2)] ='*'
    sst[int(len(sst)/2)-1]='*'
else:
    sst[int(len(sst)/2)] ='*'
for i in range(0,len(sst)):
    print(sst[i],end='')
