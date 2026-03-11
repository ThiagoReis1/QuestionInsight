s = input("String a ser digitada: ")
s2 = ''
for i in s:
	if(i.islower()):
		s2 += i.upper()
	else:
		s2 += i.lower()
print(s2)