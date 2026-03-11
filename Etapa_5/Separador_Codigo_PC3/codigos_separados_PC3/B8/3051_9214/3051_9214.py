minu = float(input("digite o consumo: "))

if minu >0 and minu <150:
	valor = minu * 0.60 + 5.00
elif minu >150 and minu <250: 
	valor = minu * 0.65 + 8.00
elif minu >250 and minu <350:
	valor = minu * 0.70 + 12.00
elif minu >350:
	valor = minu * 0.75 + 16.00
print(round(valor, 2))