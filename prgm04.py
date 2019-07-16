k1,l1=map(str,input().split())
yas=0
if len(k1)>len(l1):
  k1,l1=l1,k1
p1=0
while p1<len(k1):
  yas+=(ord(l1[p1])-ord(k1[p1]))
  p1+=1
for p1 in range(p1,len(l1)):
  yas+=ord(l1[p1])-ord('a')+1
print(yas)
