x1=int(input())
y1=[]
for i in range(x):
  y1.append(input())
  a1,b1,flag ='',0,False
for m1 in y1[0]:
  for n1 in y1[1:]:
    if len(n1)==b:
      flag=True
      break
    if n1[b1]!=m:
      break
  else:
    a1+=m
  if flag:
      break
  b1+=1
print(a1)
