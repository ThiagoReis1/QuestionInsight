salario = float(input("salario atual: "))
codigo = int(input("codigo correspondente ao cargo de um funcionario: "))

print("Entradas: R$ ", salario, "e codigo ", codigo )

if ((salario>0) and ((codigo == 101) or (codigo == 102) or (codigo == 103) or (codigo == 104))):
	if(codigo == 101):
		sn = salario + (salario*0.008)
		sn = round(sn,2)
		print("Novo salario: R$ ", sn)
	elif(codigo == 102):
		sn = salario + (salario*0.0065)
		sn = round(sn,2)
		print("Novo salario: R$ ", sn)
	elif(codigo == 103):
		sn = salario + (salario*0.0060) 
		sn = round(sn,2)
		print("Novo salario: R$ ", sn)
	else:
		sn = salario + (salario*0.0055)
		sn = round(sn,2)
		print("Novo salario: R$ ", sn)
else:
	print("Dados invalidos")