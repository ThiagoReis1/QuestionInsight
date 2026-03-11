salario=float(input("digite o valor de seu salario :"))
codigo=int(input("digite o codigo de seu cargo :"))
if(codigo==101):
	novo=((salario*((0.8)/100))+salario)
	print("Entradas: R$",salario,"e codigo",codigo)
	print("Novo salario: R$",novo)
elif(codigo==103):
	novo=((salario*(0.60)/100)+salario)
	print("Entradas: R$",salario,"e codigo",codigo)
	print("Novo salario: R$",round(novo,2))
elif(codigo==102):
	novo=((salario*(0.65)/100)+salario)
	print("Entradas: R$",salario,"e codigo",codigo)
	print("Novo salario: R$",round(novo,2))
elif(codigo==104):
	novo=((salario*(0.55)/100)+salario)
	print("Entradas: R$",salario,"e codigo",codigo)
	print("Novo salario: R$",round(novo,2))
else:
	print("Entradas: R$",salario,"e codigo",codigo)
	print("Dado invalido")