val_ant = float(input("valor do produto antigo: "))

if val_ant <= 100:
	print(round((val_ant + (val_ant * 5 / 100)),2),"ryous")
	print("Aumento de 5 porcento")
else:
	print(round((val_ant + (val_ant * 15/100)),2),"ryous")
	print("Aumento de 15 porcento")