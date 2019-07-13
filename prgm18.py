    
def armstrong(n1):
    sum1= 0
    for i in n1:
        sum1 += (int(i)**3)
    return sum1

nj1, nj2 = [int(x) for x in input().split()]
a1 = []
for i in range(nj1,nj2):
    if (armstrong(str(i))==i):
        a1.append(str(i))
print(" ".join(a1))
