m = float(input("Consumo: "))

if m < 100:
	c = m * 1.2
else:
	c = m * 1.4 + 25

print(round(c,2))