y,ab=map(int,input().split())
for i in range(y+1,ab):
	for n in range(2,i):
		if(i%n==0):
			break
	else:
		print(i,end=" ")
