m=int(input())
r=[]
for i in range(m):
  r.extend(list(map(int,input().split())))
print(*sorted(r))
