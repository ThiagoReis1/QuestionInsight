c = float(input())
tarifa = 0.0
taxa = 0.0
if c <= 150:
	tarifa = 0.60
	taxa = 5.0
elif c <= 250:
	tarifa = 0.65
	taxa = 8.0
elif c <= 35:
	tarifa = 0.70
	taxa = 12.
else:
	tarifa = 0.75
	taxa = 16.0
valor = c*tarifa+taxa
print(valor)	