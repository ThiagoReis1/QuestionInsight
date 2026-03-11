x = float(input("min: "))


valor = x

if (0 <= x <= 100):
	valor = (valor * 1.2) + 1
	
elif (100 < x <= 200):
	valor = (valor * 1.3) + 10
	
elif (x < 200 <= 300):
	valor = (valor * 1.40) + 20
	
elif (x > 300):
	valor = (valor * 1.50) + 25

print(round(valor, 2))
		