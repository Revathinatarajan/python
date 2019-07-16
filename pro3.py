m,r=map(int,input().split())
arr1=list(map(int,input().split(None,a)[:a]))
f=[]
for i in range(r):
  d,g=map(int,input().split())
  f.append(min(arr[d-1:g]))
for i in f:
  print(i)
