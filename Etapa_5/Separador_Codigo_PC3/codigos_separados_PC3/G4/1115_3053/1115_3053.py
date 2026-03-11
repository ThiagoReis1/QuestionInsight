s = float(input("Salario atual: "))
c = int(input("codigo: "))
if (s>0):
	if (c==101):
		n = s + s*((0.80)/100)
		print("Entradas: R$" , s , "e codigo" , c)
		print("Novo salario: R$" , round(n, 2))
	elif (c==102):
		n = s + s*((0.65)/100)
		print("Entradas: R$" , s , "e codigo" , c)
		print("Novo salario: R$" , round(n, 2))
	elif (c==103):
		n = s + s*((0.60)/100)
		print("Entradas: R$" , s , "e codigo" , c)
		print("Novo salario: R$" , round(n, 2))
	elif (c==104):
		n = s + s*((0.55)/100)
		print("Entradas: R$" , s , "e codigo" , c)
		print("Novo salario: R$" , round(n, 2))
	else:
		print("Entradas: R$" , s , "e codigo" , c)
		print("Dados invalidos")
else:
	print("Entradas: R$" , s , "e codigo" , c)
	print("Dados invalidos")

	