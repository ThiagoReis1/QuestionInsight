#taxa de 30 reais por cliente mesmo que nao tenha consumo
#se consumir menos de 10m³, a tarifa é de 3,00 reais por m³
#se consumir 10m³ ou mais é cobrada a tarifa de 3,50 reais por m³

consumo_agua = float(input("Qual o consumo de agua? "))

if (consumo_agua < 10):
	print(3.00 * consumo_agua + 30.00)
else:
	print(3.50 * consumo_agua + 30.00)