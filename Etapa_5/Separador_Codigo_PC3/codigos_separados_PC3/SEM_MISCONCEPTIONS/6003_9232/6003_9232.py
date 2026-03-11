compra = float(input("quantas comprou? "))
total1 = float(compra * 1.20)
total2 = float(compra * 0.90)

if (compra >= 5):
	print(round(total2, 2))
	
else:
	print(round(total1, 2))