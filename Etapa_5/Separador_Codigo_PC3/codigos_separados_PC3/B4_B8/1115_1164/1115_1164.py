salario = float(input("qual o seu salario: "))
codigo = int(input("digite o codigo do seu cargo: "))
if(salario<=0):
	print("Entradas:","R$",salario,"e","codigo",codigo)
	print("Dado invalido")
elif(101 > codigo > 104):
	print("Entradas:","R$",salario,"e","codigo",codigo)
	print("Dado invalido")
elif(101):
	novo_salario = float((salario * 0.8/100) + salario)
	print("Entradas:","R$",salario,"e","codigo",codigo)
	print("Novo salario:","R$",novo_salario)
elif(102):
	novo_salario  = float((salario * 0.65/100) + salario)
	print("Entradas:","R$",salario,"e","codigo",codigo)
	print("Novo salario:","R$", novo_salario)
elif(103):
	novo_salario = float((salario * 0.6/100) + salario)
	print("Entradas:","R$",salario,"e","codigo",codigo)
	print("Novo salario:","R$", novo_salario)
elif(104):
	novo_salario = float((salario * 0.55/100) + salario)
	print("Entradas:","R$",salario,"e","codigo",codigo)
	print("Novo salario:","R$", novo_salario)