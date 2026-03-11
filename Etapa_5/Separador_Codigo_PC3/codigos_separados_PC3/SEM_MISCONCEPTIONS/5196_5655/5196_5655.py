valan = float(input("Valor do produto: "))

if (valan > 100.00):
	valno = valan + (valan * 0.15)
	print(round(valno, 2), "ryous")
	print("Aumento de 15 porcento")
else:
	valno = valan + (valan * 0.05)
	print(round(valno, 2), "ryous")
	print("Aumento de 5 porcento")
