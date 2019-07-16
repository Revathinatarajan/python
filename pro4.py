p,q=map(int,input().split())
lis=list(map(int,input().split()))
for i in range(q):
    r,m=map(int,input().split())
    t1 = l[r-1:m]
    u1 = t[0]
    for i in range(1,len(t1)):
        u1 = u1 ^ t1[i]
    print(u1)

