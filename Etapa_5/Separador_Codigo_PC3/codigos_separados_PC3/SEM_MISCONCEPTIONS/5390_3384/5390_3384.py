from numpy import *

etiqueta = input("digite a etiqueta: ")

i = 0
total = 0

while i < len(etiqueta):
	if etiqueta[i] in 'AEIOU':
		total = total + 0.19
	else:
		total = total + 0.23
	i = i + 1
print(round(total, 2))