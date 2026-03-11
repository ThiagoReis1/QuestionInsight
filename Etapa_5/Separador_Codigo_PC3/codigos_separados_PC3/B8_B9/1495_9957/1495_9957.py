# area input

area = int(input())

if area < 10000:
	valor = area * 6.00 + 100.00

elif area >= 10000 and area < 20000:
	valor = area * 5.50 + 150.00

elif area >= 20000 and area < 30000:
	valor = area * 5.00 + 200.00
	
elif area >= 30000:
	valor = area * 4.50 + 250.00
	
valor_round = round(valor, 2)

print(valor_round)