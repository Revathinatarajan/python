m=input()
r=m.lstrip('-').replace('.','',1).isdigit()
if(r==True):
	print("yes")
else:
	print("No")
