a1,b1 = map(int,input().split())
c1 = list(map(int,input().split()))
d1 = []
for i in range(0,b1):
  i = list(map(int,input().split()))
  d1.append(i)
for i in d1:
  e1 = c1[i[0] - 1:i[1]]
  f1 = e1[0]
  for j in range(0,len(e1) - 1):
    f1 = f1 ^ e1[j + 1]
  print(f1)
