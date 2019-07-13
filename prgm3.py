x2=input()
if((x2>='a' and x2<='z') or (x2>='A' and x2<='Z')):
  x2=x2.lower()
  if(x2=='a' or x2=='e' or x2=='i' or x2=='o' or x2=='u'):
     print("Vowel")
  else:
     print("Consonant")
else:
    print("invalid")
