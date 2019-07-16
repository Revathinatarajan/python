r=int(input())
m=0
for j in range(0,r):
  if(pow(2,j)>r):
    break
  m=r-pow(2,j)
print(m)
