tipo = input(" ")
quant = int(input("insira um numero: "))
S = int(input("insira a quantidade de sucos: "))

if(tipo == 'C'):
	preco = (quant * 2) + (S * 6)
	print(round(preco, 2))
else:
	preco = (quant * 4.5) + (S * 6)
	print(round(preco, 2))