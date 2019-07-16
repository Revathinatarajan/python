n=int(input())
l=[]
for i in range(n):
    r=input()
    m=list(map(int,h.split()))
    l=l+m
l.sort()
for i in l:
    print(i,end=" ")
