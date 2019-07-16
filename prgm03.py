p1,a1=input().split()
h1=abs(len(p)-len(a1))
for i in range(len(p1)):
  if len(a1)==1 and a1[i] in p1:
    break
  if p1[i]!=a1[i]:
    h1=h1+1
print(h1)
