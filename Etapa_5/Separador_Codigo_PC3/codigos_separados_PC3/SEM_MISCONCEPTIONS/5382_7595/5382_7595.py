from numpy import *
rotulo = input("Rotulo: ").upper()

i = 0
custo = 0

while(i < len(rotulo)):
	if(rotulo[i] == "A" or rotulo[i] == "E" or rotulo[i] == "I" or rotulo[i] == "O" or rotulo[i] == "U"):
		custo = custo + 0.25
	else:
		custo = custo + 0.27
	i = i + 1
print(round(custo,2))