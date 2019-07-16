m,a1,d1=map(int,input().split())
sum=0
for i in range (n):
	sum=sum+a1
	a1=a1+d1
print(sum)
