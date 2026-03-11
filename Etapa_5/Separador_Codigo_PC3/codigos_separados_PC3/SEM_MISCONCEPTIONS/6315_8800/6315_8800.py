from numpy import *

compra = input("digite as letras: ").upper()

total = 0

cont = 0
m = 0
s = 0
i = 0

while i < len(compra):
	if compra[i] == "I":
		total = total + 3.75
		cont = cont + 1

	
	if compra[i] == "M":
		total = total + 4.50
		m = m + 1

	
	if compra[i] == "S":
		total = total + 2.90
		s = s + 1

	i = i + 1

print(round(total, 2), cont, m, s)