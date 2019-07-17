m=int(input())
r=list(map(int,input().split()))
mj1=r[:m//2]
mj2=r[m//2:]
if(sum(mj1)//len(mj1)==sum(mj2)//len(mj2)):
	print('yes')
	exit()
print('no')
