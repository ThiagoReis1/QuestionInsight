deposito = float(input("deposito: "))
meses = int(input("meses: "))
cont = 0
while (meses != cont):
	deposito = deposito * 101 / 100
	cont = cont + 1
	print(round(deposito,2))