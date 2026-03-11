medida = input("")
valor = float(input(""))

if (medida.upper() == "K"):
	mg = 2.35215 * valor
	print(round(mg, 2))
else: 
	kl = valor / 2.35215
	print(round(kl, 2))
	
	