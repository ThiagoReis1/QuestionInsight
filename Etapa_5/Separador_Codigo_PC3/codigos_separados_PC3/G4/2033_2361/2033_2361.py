ua = str(input("Unidade Acadêmica: "))
x = 0
while (ua.upper() != "S"):
	if (ua.upper() == "ICOMP"):
		x = x + 1
	
	ua = str(input("Unidade Acadêmica: "))
print (x)