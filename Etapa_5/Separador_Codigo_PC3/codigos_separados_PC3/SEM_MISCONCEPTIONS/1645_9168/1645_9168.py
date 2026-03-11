from numpy import *

valor = array(eval(input("Escreva um valor: ")))
cont = 0
for i in range(size(valor)):
	if valor[i] >= 2000:
		cont += 1
print(cont)
j = 0
contador = zeros(cont, dtype = int)
for i in range(size(valor)):
	if valor[i] >= 2000:
		contador[j] += i
		j += 1
print(contador)
	