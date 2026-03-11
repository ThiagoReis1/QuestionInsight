c= input("casa: ")
soma= 0
while (c.upper() != "S" ):
	if c.upper() == "PRETA":
		soma = soma + 1
		c= input("casa: ")
	else:
		c= input("casa: ")
print(soma)