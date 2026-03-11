consumo = float(input("valor de consumo: "))

g1 = consumo * 10/100
g2 = consumo * 6/100
t1 = consumo + (g1)
t2 = consumo + (g2)
if consumo <= 300.00:
	print(round(t1, 2))
else: 
	print(round(t2, 2))