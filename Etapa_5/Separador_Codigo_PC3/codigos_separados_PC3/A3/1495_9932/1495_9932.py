area = float(input())
valor = 0
if 0 <= area <= 10000:
	valor = area*6.00 + 100.00
	print(round(valor,2))
elif 10000 < area <= 20000:
	valor = area*5.50 + 150.00
	print(round(valor,2))
elif 20000 < area <= 30000:
	valor = area*5.00 + 200.00
	print(round(valor,2))
else:
	valor = area*4.50 + 250.00
	print(round(valor,2))