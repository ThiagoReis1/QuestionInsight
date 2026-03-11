from numpy import *

cabelo = input()

cabelo = cabelo.upper()
cabelo = cabelo.split(",")

saida = zeros(5, dtype)

for i in cabelo:
	if (i == "P"):
		saida[0] = saida[0] + 1
	elif (i == "C"):
		saida[1] = saida[1] + 1
	elif (i == "R"):
		saida[2] = saida[2] + 1
	elif (i == "L"):
		saida[3] = saida[3] + 1
	else:
		saida[4] = saida[4] + 1
		
print (max(saida))
print (saida)