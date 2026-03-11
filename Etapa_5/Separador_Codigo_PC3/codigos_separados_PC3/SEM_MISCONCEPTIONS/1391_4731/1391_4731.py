var1 = float(input("consumo de energia: "))
if(var1 <= 150):
	total = ((var1 * 0.60) + 5)
else:
	total = ((var1 * 0.75) + 16)
print(round(total, 2))
	