a1,b1=map(int,input().split())
for i in range(a1,b1):
  sum1=0
  temp1=i
  while(temp1>0):
    c1=temp1%10
    sum1=sum1+c**3
    temp1=temp1//10
  if(i==sum1):
    print(sum1,end=" ")
