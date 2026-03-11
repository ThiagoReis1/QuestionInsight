from numpy import*

m = array(eval(input('matriz de notas: '))) #matriz
i = 0
j = 0
menor = -1
for i in range(shape(m)[0]): #vai ler toda a linha
	mvl = max(m[i,:])
	if menor == -1:
		menor = mvl
	else:
		if menor < mvl:
			menor = mvl
print(menor)			