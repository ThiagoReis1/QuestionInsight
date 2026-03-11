from numpy import *
matriz = array(eval(input("Tempo de chegada: ")))
i = 0
cont = 0
for i in range(size(matriz)):
	if matriz[i] == min(matriz):
		cont = i
print(cont)