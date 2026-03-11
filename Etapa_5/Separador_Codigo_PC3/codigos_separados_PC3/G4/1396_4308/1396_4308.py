a = float(input("valor consumido: "))

if (a <= 300.00):
	b = 0.10 * a
	total = a + b
else:
	c = 0.06 * a
	total = a + c
print(round(total,2))

