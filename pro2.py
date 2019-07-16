a1,b1=map(int,input().split())
arr1=list(map(int,input().split(None,a)[:a]))
f=[]
for i in range(b1):
  d,g=map(int,input().split())
  f.append(sum(arr1[d-1:g]))
for i in f:
  print(i)
