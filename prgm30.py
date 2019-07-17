m=[]
r=[]
for i in range(2):
	x1,y1=map(int,input().split())
	m.append(x1)
	r.append(y1)
print(abs(m[0]-m[1]),abs(r[0]-r[1]),sep=' ')
