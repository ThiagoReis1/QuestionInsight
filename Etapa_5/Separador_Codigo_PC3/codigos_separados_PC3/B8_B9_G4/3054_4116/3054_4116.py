H = int(input("Horas trabalhadas: "))

if (H < 10):
   pg = (H * 50) + 500
   print(float(round(pg, 2)))
elif (H >= 10)	and (H < 20):
	pg = (H * 60) + 600
	print(float(round(pg, 2)))
elif (H >= 20)	and (H < 30):
	pg = (H * 70) + 700
	print(float(round(pg, 2)))
elif (H >= 30):
	pg = (H * 80) + 800
	print(float(round(pg, 2)))