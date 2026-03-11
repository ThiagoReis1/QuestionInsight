area = float(input("area a ser coberta:"))

if area != 0:
	if(area <= 100):
		custo = 2.00
		adubo = 100.00	
		valor = area * custo + adubo
		print(round(valor,2))
	elif area <= 2500 and area > 100:
		custo = 1.80
		adubo = 150.00		
		valor = area * custo + adubo
		print(round(valor,2))
	elif area <= 10000 and area > 2500:
		custo = 1.50
		adubo = 200.00
		valor = area * custo + adubo
		print(round(valor,2))
	elif area > 10000:
		custo = 1.20
		adubo = 250.00
		valor = area * custo + adubo
		print(round(valor,2))