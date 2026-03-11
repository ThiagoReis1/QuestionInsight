cons = float(input('consumo: '))
if cons < 10.0:
	tar = 3.0
	taxa = 15.0
elif (cons > 10.0) and (cons < 15.0):
	tar = 3.5
	taxa = 20.0
elif (cons > 15.0) and (cons < 20.0):
	tar = 4.0
	taxa = 25.0
elif (cons > 20):
	tar = 4.5
	taxa = 30.0
valor = (cons * tar) + taxa
print(round(valor, 2))