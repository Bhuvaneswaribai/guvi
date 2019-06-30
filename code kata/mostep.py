n1 = input()
n2y = []
for x in range(len(n1)):
  n2y.append(n1.count(n1[x]))
x = n2y.index(max(n2y))
print (n1[x])
