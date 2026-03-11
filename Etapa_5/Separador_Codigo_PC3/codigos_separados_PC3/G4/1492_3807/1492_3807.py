h = int(input("horas:"))

if (h >= 0 and h <= 10):
	pg = (h * 50) + 500
	print(round(pg, 2))
	
elif(h > 10 and h <= 20):
	pg = (h * 60) + 600
	print(round(pg, 2))
	
elif(h > 20 and h <= 30):
	pg = (h * 70) + 700
	print(round(pg, 2))
	
elif(h > 30):
	pg = (h * 80) + 800
	print(round(pg, 2))
	
else:
	print("Carga invalida")
	


