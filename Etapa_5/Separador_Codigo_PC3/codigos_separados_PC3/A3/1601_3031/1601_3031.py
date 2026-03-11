tempos = eval(input(""))

indice = 0
minimo = tempos[0]

for i in range(0, len(tempos)):
	if(tempos[i] < minimo):
		minimo = tempos[i]
		indice = i

print(indice)

