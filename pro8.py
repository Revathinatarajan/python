n,m=map(int,input().split())
l=[]
for i in range(n):
  l.append(input())
for i in range(len(l)):
  if('0' in l[i]):
    l[i]=l[i].replace('0','')
  l[i]=l[i].replace(' ','')
length=[]
for i in l:
  if(len(i)>0):
    length.append(len(i))
m=min(length)
r='1 '*m
r=r.strip()
for i in range(m):
  print(r)
