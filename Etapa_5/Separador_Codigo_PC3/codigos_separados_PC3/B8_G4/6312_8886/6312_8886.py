from numpy import *
alimentos = input(" ")
qtd = 0
i = 0
cont = 0

while i < len(alimentos):
	if alimentos[i] == "B":
		qtd = qtd + 3.75
		i = i + 1
		
	elif alimentos[i] == "C":
		qtd = qtd + 7.90
		i = i + 1
		
	elif alimentos[i] == "E":
		qtd = qtd + 9.85
		i = i + 1
		

print(round(qtd,2),cont)