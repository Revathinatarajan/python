import math
p,q=map(int,input().split())
rr1=[]
ss1=list(map(int,input().split()))
for i in range(0,q):
        uu,vv =map(int,input().split())
        rr1.append([uu,vv])
for i in rr1:
        xx=i[0]-1
        yy=i[1]-1
        print(math.gcd(ss1[xx],ss1[yy]))
