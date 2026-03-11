valor = float(input("valor consumido no restaurante: "))

if valor <= 300:
	gorjeta = valor * 0.1
	total = valor + gorjeta
	
if valor > 300:
	gorjeta = valor * 0.06
	total = valor + gorjeta
	
print(round(total, 2))	