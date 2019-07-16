asd1,ssd1=map(int,input().split())
law1=list(map(int,input().split()))
asd1=[]
law1.insert(0,0)
for p1 in range(ssd1):
     vim1=[]
     sha1=0
     but1,zee1=map(int,input().split())
     for i in range(but1,zee1+1):         
         sha1^=law1[i]     
     asd1.append(sha1)
for p1 in asd1:
     print(p1)
