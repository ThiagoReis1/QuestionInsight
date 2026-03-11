from numpy import*

numeros = array(eval(input()))
i = 0

M = numeros[0:-1]**(1/6)

while(i<size(numeros)):
	print(round(M, 2))