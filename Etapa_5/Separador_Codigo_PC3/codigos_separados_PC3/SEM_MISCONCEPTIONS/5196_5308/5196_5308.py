antigo = float(input(" valor antigo: "))

porc_5 = antigo * 0.05

porc_15 = antigo * 0.15

if ( antigo <= 100.00):
	novo = antigo + porc_5
	print(round(novo, 2),"ryous")
	print("Aumento de 5 porcento")
else:
	(antigo > 100.00)
	novo = antigo + porc_15
	print(round(novo, 2),"ryous")
	print("Aumento de 15 porcento")

