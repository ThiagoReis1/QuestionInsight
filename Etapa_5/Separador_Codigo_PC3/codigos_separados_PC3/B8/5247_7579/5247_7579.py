sal = float(input(":"))
cod = int(input(":"))

if cod >= 101 and cod <=104:
	if cod == 101:
		total = sal +(sal * 0.008)
		
	elif cod == 102:
		total = sal +(sal * 0.0065)
		
	elif cod == 103:
		total = sal +(sal * 0.006)
		
	elif cod == 104:
		total = sal +(sal *0.0055)
		
	print("Novo salario: R$ ", round(total,2))
	
else:
	print("Dados invalidos")