preco_a= float(input("Insira o valor na abertura da bolsa"))
preco_f= float(input("Insira o valor no fechamento da bolsa"))
if (preco_f > preco_a):
	print("saldo positivo")
elif (preco_f < preco_a):
	print("saldo negativo")
elif (preco_f == preco_a):
	print("sem variacao")