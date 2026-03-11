abertura= float(input("Digite o preco da acao:"))
fechamento= float(input("Digite o preco da acao:"))

diferenca= (fechamento - abertura)
percentual= round(diferenca/100, 2)

if(percentual>0):
	print("saldo positivo")
else:
	print("saldo negativo")
	
