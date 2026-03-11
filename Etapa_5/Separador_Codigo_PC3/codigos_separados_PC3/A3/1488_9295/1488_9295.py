x = int(input(""))
valor = 0

if x > 0 and x <= 100:
	valor = x * 1.20 + 1.00
elif x > 100 and x <= 200:
	valor = x * 1.30 + 10.00
elif x > 200 and x <= 300:
	valor = x * 1.40 + 20.00
else:
	valor = x * 1.50 + 25.00

print(round(valor,2))
	
	