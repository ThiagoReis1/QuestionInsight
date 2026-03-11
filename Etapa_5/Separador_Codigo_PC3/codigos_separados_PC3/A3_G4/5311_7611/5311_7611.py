di = float(input('Deposito inicial: '))
temp = int(input('numero de meses de aplicacao: '))

cont = 0
i = 0

while (cont != temp):
	di = di + (di * 0.012)
	cont = cont + 1
	print(round(di,2))