m1=int(input())
b1=m1
n1=0
while m1!=0:
  c1=m1%10
  n1=n1*10+c1
  m1=m1//10
if(n1==b1):
  print("yes")
else:
  print("no")
