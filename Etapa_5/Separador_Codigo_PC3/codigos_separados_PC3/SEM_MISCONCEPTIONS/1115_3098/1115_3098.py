#salarios e codigos (entradas)
sal=float(input("salario"))
cod=int(input("codigo"))
print("Entradas: R$ ",sal," e codigo ",cod)
if(cod==101 and sal>=0):#para entrar na condicional
	reajuste=(sal*0.008) + sal
	print("Novo salario: R$ ",round(reajuste,2))
elif(cod==102 and sal>=0):
	reajuste=(sal*0.0065) + sal
	print("Novo salario: R$ ",round(reajuste,2))
elif(cod==103 and sal>=0):
	reajuste=(sal*0.006) + sal
	print("Novo salario: R$ ",round(reajuste,2))
elif(cod==104 and sal>=0):
	reajuste=(sal*0.0055) + sal
	print("Novo salario: R$ ",round(reajuste,2))
else:
	print("Dados invalidos")

