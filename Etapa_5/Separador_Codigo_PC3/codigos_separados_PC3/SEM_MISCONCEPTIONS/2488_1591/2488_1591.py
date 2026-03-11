salario = float(input())

print("Entrada: R$",salario,)


if(salario <= 800.00):
	print("Novo salario: R$ ",round(salario * 1.50, 2))
	
elif(800.00 < salario <= 1000.00):
	print("Novo salario: R$ ",round(salario * 1.40, 2))
	
elif(1000.00 < salario <= 1200.00):
	print("Novo salario: R$ ",round(salario * 1.30, 2))
	
elif(1200.00 < salario <= 1400.00):
	print("Novo salario: R$ ",round(salario * 1.20, 2))
	
elif(1400.00 > salario <= 1600.00):
	print("Novo salario: R$ ",round(salario * 1.10, 2))
	
elif(salario > 1600.00):
	print("Novo salario: R$ ",round(salario * 1.05, 2))
	
else:
	print("Dado invalido")
	