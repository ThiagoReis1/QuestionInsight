tempo_permanencia = float(input())

preco_fixo = 5

if tempo_permanencia < 2:
	total = preco_fixo + 1.25
elif tempo_permanencia == 2:
	total = preco_fixo + 2.25
elif tempo_permanencia > 2:
	total = preco_fixo + 3.25
print (round(total, 2))

