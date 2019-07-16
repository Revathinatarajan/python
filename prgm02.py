p1,k1=input().strip().split(" ")
k1=int(k1)
j=0;
while j<len(p1)-1 and k1:
    if(p1[j]>p1[j+1]):
        k1-=1
        p1=p1[:j]+p1[j+1:]
        if(j!=0):
            j-=1
    else:
        j+=1
s1=p1[:len(p1)-k1]
print(s1)
