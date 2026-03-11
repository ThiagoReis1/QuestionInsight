taxa_semconsumo = 30
tarifa1 = 3.0
tarifa2 = 3.50

consumo = int(input("Valor do consumo: "))

consumo1 = (consumo * tarifa1) + taxa_semconsumo
consumo2 = (consumo * tarifa2) + taxa_semconsumo

if (consumo < 10):
	print(round(consumo1,2))

else:
	print(round(consumo2,2))