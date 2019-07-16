import sys, string, math
m1,m2 = input().split()
r1 = len(m1)
r2 = len(m2)
if r2 > r1 :
    i = 0
    while i<r1 and m1[i] == m2[i] :
        i += 1
    print(r2-i)
elif r2 == r1 :
    i = 0
    while i<r2 and m1[i] == m2[i] :
        i += 1
    print(r2-i)
else :

    i = 0
    while i<r2 and m1[i] == m2[i] :
        i += 1
    m31 = m1[i:]
    m32 = m2[i:]
    L = list(m31)
    k = 0
    for c in m32 :
        if c in L :
            k += 1
            L.remove(c)
    print(r1-i-k)
