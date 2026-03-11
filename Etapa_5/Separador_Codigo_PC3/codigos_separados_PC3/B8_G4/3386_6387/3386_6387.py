from math import * 

r = input("Unidade de medida: ")
a = float(input("Valor do angulo: "))

if r == "R":
	gr = a / 0.0174533
	print(round(gr,2))
elif r == "G":
	rad = 0.0174533 * a
	print(round(rad,2))