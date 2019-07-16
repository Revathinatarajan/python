a1=input().split()
t1=int(a1[0])
con=int(a1[1])
l1=input().split()
l1=[int(i) for i in l1]
l1=sorted(l1,reverse=True)
temp=0
count=0
for i in range(0,len(l1)):
  while True:
    if(temp==con):
      break
    elif(temp>con):
      count-=1
      temp-=l1[i]
      break
    elif(temp<con):
      temp+=l1[i]
      count+=1
print(count)
