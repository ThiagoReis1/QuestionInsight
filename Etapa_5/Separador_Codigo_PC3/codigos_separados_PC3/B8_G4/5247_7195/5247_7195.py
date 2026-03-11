sal=float(input())
cod=int(input())

print("Entradas: R$", sal, "e codigo", cod )

if sal < 0 or not(cod == 101 or cod==102 or cod==103 or cod==104):
	print("Dados invalidos")

elif cod==101:
	a=(sal/100)*0.80
	rea=sal+a
	print("Novo salario: R$", round(rea,2))
elif cod==102:
	a=(sal/100)*0.65
	rea=sal+a
	print("Novo salario: R$", round(rea,2))
elif cod == 103:
	a=(sal/100)*0.6
	rea=sal+a
	print("Novo salario: R$", round(rea,2))
elif cod == 104:
	a=(sal/100)*0.55
	rea=sal+a
	print("Novo salario: R$", round(rea,2))





	