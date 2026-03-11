valor = float(input("digite valor de venda: "))
valorum = valor * 5 / 100
valordois = valor * (10 / 100) - (1000 * 5 / 100)
if(valor > 1000):
	print(round(valordois,2))
else:
	print(round(valorum,2))