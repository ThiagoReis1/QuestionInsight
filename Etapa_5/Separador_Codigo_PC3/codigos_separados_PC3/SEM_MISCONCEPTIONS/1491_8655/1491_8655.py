peso = float(input(""))

if peso<= 5000:
	tarifa = 0.03
	taxa = 20.0
elif peso <= 6000:
	tarifa = 0.04
	taxa = 25.0
elif peso <= 7000:
	tarifa = 0.05
	taxa = 30.0
else:
	tarifa = 0.06
	taxa = 35.0

valor = peso * tarifa + taxa
print(round(valor , 2))