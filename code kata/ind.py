n1=int(input())
lt1=list(map(int,input().split()))
for i in range (len(lt1)):
  if(lt1[i]>lt1[i+1]):
    break
print(i)
