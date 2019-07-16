a=int(input())
r=list(map(int,input().split()))
m=0
for i in range(0,a):
  for j in range(0,i):
    if(r[j]<r[i]):
      m=m+r[j]
print(m)
