from numpy import *
notas = array(eval(input("Notas: ")))
cont = 0
n = size(notas)
for i in range(n):
	if(notas[i] >= 5):
		cont = cont + 1
aprov = zeros(cont, dtype = int)
j = 0
for i in range(n):
	if(notas[i] >= 5):
		aprov[j] = i
		j = j + 1
print(cont)
print(aprov)