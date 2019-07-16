m=int(input())
c=0
l=[]
for i in range(1,m+1):
  l.append(i)
for i in range(len(l)):
  for i in range(i+1,len(l)):
    c+=1
print(c)
