def sub(r): 
    m = len(r) 
    sub = [1]*m 
    for i in range (1 , m): 
        for j in range(0 , i): 
            if r[i] > r[j] and sub[i]< sub[j] + 1 : 
                sub[i] = sub[j]+1
    maximum = 0
    for i in range(m): 
        maximum = max(maximum , sub[i])  
    return maximum




ar1=int(input()) 
r = list(map(int,input().split()))
print (sub(r))
