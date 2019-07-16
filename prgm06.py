mn=int(input())
s=list(map(int,input().split()))
r=0
for i in range(mn):
  for j in range(i,mn):
    for k in range(j,mn):
      if(s[i]<s[j]<s[k]):
        r+=1
print(r)
