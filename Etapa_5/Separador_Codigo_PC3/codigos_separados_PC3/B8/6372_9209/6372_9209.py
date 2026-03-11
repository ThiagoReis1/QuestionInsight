from numpy import *

contador = zeros(4, dtype= int)

compras = input("Listas de compras: ").upper().split(",")

for i in range (len(compras)):
	if compras[i] == "A":
		contador[0] = contador[0] + 1
	elif compras[i] == "B":
		contador[1] = contador[1] + 1
	elif compras[i] == "L":
		contador[2] = contador[2] + 1
	elif compras[i] == "H":
		contador[3] = contador[3] + 1
print(contador)