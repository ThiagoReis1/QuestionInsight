consumo = float(input("Digite o numero:"))

if 0 <= consumo <= 150:
	valor = consumo * 0.60 + 5
	print(round(valor,2))
	
elif 150 < consumo <= 250:
	valor = consumo * 0.65 + 8
	print(round(valor,2))
	
elif 250 < consumo <= 350:
	valor = consumo * 0.70 + 12
	print(round(valor,2))
	
elif consumo > 350:
	valor = consumo * 0.75 + 16
	print(round(valor,2))