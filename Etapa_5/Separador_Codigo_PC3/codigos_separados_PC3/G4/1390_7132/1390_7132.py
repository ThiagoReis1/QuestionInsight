var1=float(input("consumo de minutos: "))

if var1 <= 100:
	c= 1.20 * var1
else:
	c= 25.00 + (1.40 * var1)
print(round(c, 2))