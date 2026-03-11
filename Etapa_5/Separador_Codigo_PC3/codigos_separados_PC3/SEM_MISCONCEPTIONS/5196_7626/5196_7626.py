valorantigo= float(input(""))

novop1= valorantigo * (5/100) + valorantigo
novop2= valorantigo * (15/100) + valorantigo


if valorantigo <= 100.000:
	print(round(novop1, 2), " ryous")
	print("Aumento de 5 porcento")
	
if valorantigo > 100.00:
	print(round(novop2, 2), "ryous")
	print("Aumento de 15 porcento")