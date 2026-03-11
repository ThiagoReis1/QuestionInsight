preco = float(input(""))

if(preco <= 50):
	valor = preco + (preco * 1)
	print(round(valor, 2))
elif((preco >= 50.01) and (preco <= 100)):
	valor = preco + (preco * 0.5)
	print(round(valor, 2))
elif((preco >= 100.01) and (preco <= 500)):
	valor = preco + (preco * 0.4)
	print(round(valor, 2))
elif(preco > 500):
	valor = preco + (preco * 0.3)
	print(round(valor, 2))