x,mn=map(int,input().split())
for i in range(x+1,mn):
	for a in range(2,i):
		if(i%a==0):
			break
	else:
		print(i,end=" ")
