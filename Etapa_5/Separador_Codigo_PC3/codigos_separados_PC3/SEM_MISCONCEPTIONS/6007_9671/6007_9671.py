quant = int(input("insira a quantidade de espigas de milho compradas: "))

if quant < 6:
	preco = quant * 1.85
else:
	preco = quant * 1.50
	
print(round(preco, 2))