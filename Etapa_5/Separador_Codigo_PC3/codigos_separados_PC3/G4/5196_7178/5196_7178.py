a = float(input("digite o preco do produto:"))

if a <= 100:
	b = (5/100 * a) + a
	print(round(b, 2), "ryous") 
	print("Aumento de 5 porcento")
else: 
	c = (15/100 * a) + a
	print(round(c, 2), "ryous")
	print("Aumento de 15 porcento")