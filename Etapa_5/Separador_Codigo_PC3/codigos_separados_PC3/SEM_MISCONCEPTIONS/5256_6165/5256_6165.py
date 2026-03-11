a = float(input("Preco da acao na abertura da bolsa: "))
b = float(input("preco da acao no fechamento da bolsa: "))

if(a > 0):
	a = a*0.10
	print("saldo positivo:", a)
elif(a < 0):
	b = a*0.10
	print("sem variacao:",b, 2))
else:
	print("saldo negativo")