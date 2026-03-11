inicial = float(input("Deposito inicial: "))
meses = float(input("Meses: "))
taxa = 1

mensal = inicial

cont = 0

while(cont < meses):
	mensal = mensal + (mensal * 0.01)
	cont = cont + 1
	print(round(mensal,2))
