qtd_m = int(input("Quantidade de Milho: "))

if qtd_m >= 6:
	total = qtd_m * 1.50
else:
	total = qtd_m * 1.85
print(round(total,2))