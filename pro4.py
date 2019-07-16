a1,b1=map(int,input().split())
lis=list(map(int,input().split()))[:a]
res=[]
while(b1):
    x1=list(map(int,input().split()))
    res.append(x1)
    b1=b1-1   
for i in res:
    ans=0
    for j in range(i[0]-1,i[1]):
       ans=ans^lis[j]
    print(ans)

