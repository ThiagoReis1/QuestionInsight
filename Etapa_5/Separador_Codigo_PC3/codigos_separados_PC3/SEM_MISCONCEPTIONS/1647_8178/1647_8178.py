from numpy import*

numeros = array(eval(input()),dtype=int)
aprovados = 0
indice_aprovados = []

for i in range(size(numeros)):
	if numeros[i] >= 70:
		aprovados += 1
		indice_aprovados.append(i)
indice_aprovados = array(indice_aprovados)

print(aprovados)
print(indice_aprovados)
	