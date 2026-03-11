salario = float(input())
cod = int(input())

if(salario >= 0):
	if(cod == 101):
		print("Novo salario: R$ "+str(round(salario * 1.008, 2)))
	elif(cod == 102):
		print("Novo salario: R$ "+str(round(salario * 1.0065, 2)))
	elif(cod == 103):
		print("Novo salario: R$ "+str(round(salario * 1.006, 2)))
	elif(cod == 104):
		print("Novo salario: R$ "+str(round(salario * 1.0055, 2)))
	else:
		print("Dados invalidos")
else:
	print("Dados invalidos")