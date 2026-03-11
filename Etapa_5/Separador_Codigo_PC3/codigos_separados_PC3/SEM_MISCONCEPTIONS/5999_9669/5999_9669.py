numero_lar = int(input("Entre com o valor de laranjas: "))

preco_1 = 0.75 * numero_lar
preco_2 = 0.60 * numero_lar

if numero_lar < 6:
	print(round(preco_1,2))

else:
	print(round(preco_2,2))
	