sal = float(input("Salario: "))
cod = int(input("Codigo Funcionario: "))
msg = "Novo salario: R$"
if sal >= 0:
	if cod == 101:
		total = sal + (sal * ( 0.8/100))
		print(msg, round(total,2))
	elif cod == 102:
		total = sal + (sal * (0.65/100))
		print(msg, round(total,2))
	elif cod == 103:
		total = sal + (sal * (0.60/100))
		print(msg, round(total,2))
	elif cod == 104:
		total = sal + (sal * (0.55/100))
		print(msg, round(total,2))
	else: 
		print("Dados invalidos")
else:
	print("Dados invalidos")