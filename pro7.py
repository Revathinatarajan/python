num=input()
a1=list(map(int,num.split()))
k1=a1[1]
h1=input()
flag=0
s1=list(map(int,h1.split()))
for i in range(0,len(s1)-1):
	for j in range(i+1,len(s1)):
		if s1[i]+s1[j]==k1:
			print("yes")
			flag=1
			break
	if flag==1:
		break
if flag!=1:
	print("no")
