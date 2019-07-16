p1=int(input())
o1=[]
for hr1 in range(0,p1):
 pan=input()
 o1.append(pan)
de=[]
for hr1 in zip(*o1):
 if(hr1.count(hr1[0])==len(hr1)):
  de.append(hr1[0])
 else:
  break
print(''.join(de))
