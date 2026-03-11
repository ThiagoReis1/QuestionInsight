from numpy import *


notas = array(eval(input("digite a nota dos alunos: ")))
cont = 0

for i in range(size(notas)):
	if notas[i] >= 5:
		cont += 1
print(cont)

aprov = zeros (cont, dtype = int)
j = 0

for i in range(size(notas)):
	if notas[i] >= 5:
		aprov [j] = i
		j+= 1
print (aprov)

			

