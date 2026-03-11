roleta = input("JOGUE: ").upper()
cont = 0
soma = 0 
while roleta != "S":	
	if roleta == "PRETA":
		cont = cont + 1 
		soma = soma + cont
	roleta = input("JOGUE: ").upper()
	
	print(soma)
		