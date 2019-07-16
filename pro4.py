m,r=map(int,input().split())
n1=list(map(int,input().split()))
m1=[]
for m in range(r):
       j=list(map(int,input().split()))
       m1.append(j)
for i in m1:
    v1=0
    for k1 in range(i[0]-1,i[1]):
        v1=v1^n[k1]
    print(v1)    

