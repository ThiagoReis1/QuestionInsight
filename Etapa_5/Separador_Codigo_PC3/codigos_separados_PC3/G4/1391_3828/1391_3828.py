kwh = float(input("digite o consumo: "))
if (kwh <= 150):
	msg = kwh * 0.6 + 5

else:
	msg = kwh * 0.75 + 16
print(msg)