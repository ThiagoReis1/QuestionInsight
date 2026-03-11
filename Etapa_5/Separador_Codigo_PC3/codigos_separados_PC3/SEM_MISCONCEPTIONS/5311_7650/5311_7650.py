dpst_inicial = float(input("Deposito inicial: "))
meses_aplic = int(input("Numero de meses a ser aplicado: "))

saldo = dpst_inicial
mes = 1

while(meses_aplic >= mes):
	saldo = (0.012 * saldo) + saldo
	mes = mes + 1
	print(round(saldo , 2))