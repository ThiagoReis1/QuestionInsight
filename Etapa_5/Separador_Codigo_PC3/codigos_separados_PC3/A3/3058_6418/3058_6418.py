area = float(input("digite a area: "))
custo = 2
fert = 100

if (0 < area < 100):
	custo = 2
	fert = 100
elif (100 <= area < 2500):
	custo = 1.8
	fert = 150
elif (2500 <= area < 10000):
	custo = 1.5
	fert = 200
else:
	custo = 1.2
	fert = 250
	
valor = area * custo + fert

print(round(valor,2))