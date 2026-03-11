consumo = int(input("valor"))
if (consumo <= 150):
	msg = 0.60 * consumo + 5.00
else:
	msg = 0.75 * consumo + 16.00
print(msg)	