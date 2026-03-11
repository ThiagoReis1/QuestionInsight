from math import *

area = int(input("informe a area a ser fertilizada: "))

if (area >= 0 and area <= 10000):
	valor = (area * 6) + 100
elif (area > 10000 and area <= 20000):
	valor = (area * 5.50) + 150
elif (area > 20000 and area <= 30000):
	valor = (area * 5) + 200
else:
	valor = (area * 4.50) + 250
	
print(round(valor, 2))