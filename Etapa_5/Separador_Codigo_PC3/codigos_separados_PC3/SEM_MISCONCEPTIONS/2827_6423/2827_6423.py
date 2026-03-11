from numpy import*
notas = array(eval(input("Notas")), dtype=float)
i = 0
for notas[i] in notas:
	if notas[i]>4 and notas[i]<5:
		notas[i]=4
	if notas[i]>9 and notas[i]<10:
		notas[i]=10
	i+=1
print(notas)