valorC=float(input("Valor Consumido: "))
if(valorC <= 300):
	gorjeta=0.10*valorC
	total=valorC + gorjeta
	print(round(total,2))
if(valorC > 300):
	gorjeta=0.06*valorC
	total=valorC + gorjeta
	print(round(total,2))