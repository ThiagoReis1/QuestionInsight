sal = float(input("salario atual: "))
cod = int(input("codigo do cargo:"))
print("Entradas: R$", sal, "e codigo", cod)


if sal < 0 or not(cod == 101 or cod == 102 or cod == 103 or cod == 104):
	print("Dados invalidos")

elif cod == 101:
	a = (sal * 0.80)/100
	rea = sal + a
	print("Novo salario: R$", round(rea, 2))
	
elif cod == 102:
	a = (sal * 0.65)/100
	rea = sal + a
	print("Novo salario: R$", round(rea, 2))
	
elif cod == 103:
	a = (sal * 0.60)/100
	rea = sal + a
	print("Novo salario: R$", round(rea, 2))
	
elif cod == 104:
	a = (sal * 0.55)/100
	rea = (sal + a)
	print("Nova salario: R$", round(rea, 2))