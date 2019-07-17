a1=int(input())
b1=pow(2,a)
z1=[]
for i in range(b1):  
    m1=bin(i).replace("0b1","")
    z1.append(m1.zfill(a1))
    z1.sort(key=(lambda x1:x1.count('1')))
for i in z1:
    print(i)
