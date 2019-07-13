num1=int(input())
temp1=num1
add1=0
while num1>0:
    las1t=num1%10
    add1+=last1**3
    num1=num1//10
if add1==temp1:
    print('yes')
else:
    print('no')
