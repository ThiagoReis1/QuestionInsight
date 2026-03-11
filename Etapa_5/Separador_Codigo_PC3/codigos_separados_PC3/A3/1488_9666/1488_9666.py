minutos = [101,201,301]
tarifa = [1.2, 1.3, 1.4, 1.5]
taxa = [1.0, 10.0, 20.0, 25.0]

consumo = int(input())
total = 0.0

if consumo < 101:
	total = (consumo * tarifa[0]) + taxa[0]
	
elif consumo < 201:
	total = (consumo * tarifa[1]) + taxa[1]
	
elif consumo < 301:
	total = (consumo * tarifa[2]) + taxa[2]
	
else: total = (consumo * tarifa[3]) + taxa[3]
	
print(round(total, 2))
