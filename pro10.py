r,m=list(map(int,input().split()))
l1=list(map(int,input().split()))
l1.sort(reverse=True)
c1=0
for i in l1:
  if m==0:
    break
  q=m//i
  c1+=q1
  m=m-i*(q)
print(c1)
