area = int(input("Digite a area a ser coberta em metros quadrados: "))

if(area >= 0 and area <= 100):
	custo = 2
	adubo = 100
	valor = float(area * custo + adubo)
elif(area > 100 and area <= 2500):
	custo = 1.80
	adubo = 150
	valor = float(area * custo + adubo)
elif(area > 2500 and area < 10000):
	custo = 1.5
	adubo = 200
	valor = float(area *custo + adubo)
elif(area > 10000):
	custo = 1.20
	adubo = 250
	valor = float(area * custo + adubo)
print(round(valor,2))