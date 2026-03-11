ce = float(input("Consumo de energia: "))
if(ce <= 150):
	tc = 0.6 * ce + 5
else:
	tc = 0.75 * ce + 16
print(tc)