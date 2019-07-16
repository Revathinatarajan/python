m,r=input().split()
m=int(m)
r=int(r)
k1=[]
l1=input().split()
1l=[int(i) for i in l1]
for i in range(r):
  s1=0
  u1,v1=input().split()
  u1=int(u1)
  v1=int(v1)
  for i in range(u1-1,v1):
    m^=l1[i]
  k.append(s1)
for i in k1:
  print(i)
