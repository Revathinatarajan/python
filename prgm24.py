mm = int(input())
rr = list(map(int,input().split()[:mm]))
xx = sorted(rr)
for i in xx:
    print(i,end=" ")
