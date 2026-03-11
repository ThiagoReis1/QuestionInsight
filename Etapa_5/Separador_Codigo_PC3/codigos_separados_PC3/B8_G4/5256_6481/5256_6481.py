pi = round(float(input()), 2)
pf = round(float(input()), 2)

if (pf - pi) > 0:
	print('saldo positivo')
elif (pf - pi) == 0:
	print('sem variacao')
elif (pf - pi) < 0:
	print('saldo negativo')
    