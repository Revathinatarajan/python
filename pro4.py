m1,m2=list(map(int,input().split()))
lis1=list(map(int,input().split()))
lis2=[]
while(m2):
	k1 = list(map(int,input().split()))
	lis2.append(k1)
	m2-=1
for i in lis2:
	value=0
	for j in range(i[0]-1,i[1]):
		value=value^lis1[j]
	print(value)
