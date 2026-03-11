salt=float(input())
cod=int(input())

if(not(cod==101 or cod==102 or cod==103 or cod==104)):
	print("Entradas: R$", salt, "e codigo ",cod)
	print("Dados invalidos")
elif(cod==101):
	print("Entradas: R$", salt, "e codigo ",cod)
	print("Novo salario: R$", round(salt + salt * 8/1000,2))
elif(cod==102):
	print("Entradas: R$", salt, "e codigo ",cod)
	print("Novo salario: R$", round(salt + salt * 6.5/1000,2))
elif(cod==103):
	print("Entradas: R$", salt, "e codigo ",cod)
	print("Novo salario: R$", round(salt + salt * 6/1000,2))
elif(cod==104):
	print("Entradas: R$", salt, "e codigo ",cod)
	print("Novo salario: R$", round(salt + salt * 5/1000,2))