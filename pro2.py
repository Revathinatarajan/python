m,r=list(map(int,input().split()))
lis1=list(map(int,input().split()))
for i in range(r):
  u1,v1=list(map(int,input().split()))
  print(sum(lis1[u1-1:v1]))
