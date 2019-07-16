m,r = input().split()
m,r = int(m), int(r)
L1 = [ int(x) for x in input().split()]
for i in range(0,r) :
    a1,b1 = input().split()
    a1,b1 = int(a1), int(b1)
for i in range(0,r):
    print(min(L1[a1-1:b1]))
