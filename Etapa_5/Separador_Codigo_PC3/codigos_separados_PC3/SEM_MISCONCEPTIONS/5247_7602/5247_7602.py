salario = float(input())
codigo = int(input())

if salario>0:
	if codigo == 101 or codigo == 102 or codigo == 103 or codigo == 104:
		if codigo==101:
			x = salario + (salario*0.80/100)
			print("Novo salario: R$ ",round(x,2))
		elif codigo ==102:
			x =  salario + (salario*0.65/100)
			print("Novo salario: R$ ",round(x,2))
		elif codigo==103:
			x = salario + (salario*0.60/100)
			print("Novo salario: R$ ",round(x,2))
		else:
		#elif codigo == 104 
			x = salario +(salario*0.55/100)
			print("Novo salario: R$ ",round(x,2))
	else:
		print("Dados invalidos")
else:
	print("Dados invalidos")
