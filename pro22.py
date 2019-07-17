a=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
s1=0
s2=0
res=[]
for i in range(0,a,2):
    s1=s1+arr[i]
for j in range(1,a,2):
    s2=s2+arr[j]
res.append([s1,s2])
for i in res:
    print(i[0] if i[0]>i[1] else i[1])
