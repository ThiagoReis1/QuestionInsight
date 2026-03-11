minu = float(input ("Digite o consumo: "))

if minu > 0 and minu <= 100 :
	valor= minu * 1.20 + 1.00
elif minu> 100 and minu < 200:
	valor= minu * 1.30 + 10.00
elif minu > 200 and minu < 300 :
	valor= minu * 1.40 + 20.00
elif minu > 300 :
	valor= minu * 1.50 + 25.00
print(round(valor, 2))