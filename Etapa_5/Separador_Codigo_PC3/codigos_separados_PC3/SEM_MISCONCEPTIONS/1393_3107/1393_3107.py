peso_encomenda = float(input())

if peso_encomenda <= 4999.9:
	valor_frete = peso_encomenda * 0.05
	print(round(valor_frete, 2))
else:
	valor_frete = ((peso_encomenda * 0.04) + 60)
	print(round(valor_frete, 2))