valor = float(input("quanto o funcionario vendeu?"))

menosdemil = 0.05 * valor
maisdemil = (0.05 * 1000) + (valor-1000) * 0.1

if (valor > 1000):
	print(round(maisdemil,2))
else:
	print(round(menosdemil,2))
