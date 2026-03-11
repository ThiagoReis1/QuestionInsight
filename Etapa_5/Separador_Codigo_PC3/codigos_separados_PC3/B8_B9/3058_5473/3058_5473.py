area = float(input("Informe a area: "))

if(area <= 100):
	valor = area * 2 + 100
elif(area > 100 and area <= 2500):
	valor = area * 1.80 + 150
elif(area > 2500 and area <= 10000):
	valor = area * 1.50 + 200
elif(area > 1000):
	valor = area * 1.20 + 250
		
print(round(valor,2))