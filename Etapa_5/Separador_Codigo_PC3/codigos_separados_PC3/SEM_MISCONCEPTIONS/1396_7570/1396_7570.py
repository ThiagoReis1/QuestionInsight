x = float(input(""))

if (x <= 300.00):
	g = x * 0.10
	total = g + x
	total = float(total)
	print(round(total, 2))
else:
	g = x * 0.06
	total = g + x
	print(round(total, 2))