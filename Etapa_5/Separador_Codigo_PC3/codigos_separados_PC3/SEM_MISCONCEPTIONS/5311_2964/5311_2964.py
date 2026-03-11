deposito = float(input())
qtdMeses = int(input())
i = 0
vlrTotal = deposito

while(i < qtdMeses):
	vlrTotal = vlrTotal * 1.012
	print(round(vlrTotal, 2))
	i += 1
