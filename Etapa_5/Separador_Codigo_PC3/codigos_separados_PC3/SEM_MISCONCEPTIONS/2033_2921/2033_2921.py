x= input()
x = x.upper()
a= 0
while(x != "S"):
	if (x == "ICOMP"):
		icomp = 1
	else:
		icomp = 0
	x= input()
	x = x.upper()
	a= icomp + a
print(a)