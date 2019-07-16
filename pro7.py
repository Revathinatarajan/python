x=input().split()
x=[int(i) for i in x1]
k1=x[1]
flag=False
l=input().split()
l=[int(i) for i in l]
for i in range(0,x[0]):
  for j in range(i+1,x[0]):
    t1=l[i]+l1[j]
    if(t1==k1):
      flag=True
      break
  if(flag):
    print("yes")
    break
if not(flag):
  print("no")
