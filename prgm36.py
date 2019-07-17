m=input()
r=0
for i in m:
	if i.isnumeric():
		pass
	elif i.isalpha():
		pass
	elif i.isspace():
		pass
	else:
		r+=1
print(r)
