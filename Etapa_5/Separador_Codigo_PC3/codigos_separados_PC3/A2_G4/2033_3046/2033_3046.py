x = (input().upper())

a = 0

while(x != "S"):
	if(x == "ICOMP"):
		a = a + 1
	else:
		a = a
	x = (input().upper())
print(a)