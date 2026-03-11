from numpy import *

notas = array(eval(input()))
tam = size(notas)
soma = sum(notas)
total = 0
i = 0
t = 0
while tam > i:
	parcial = notas[i] * (i + 1)
	total = total + parcial
	i = i +1
	t = t + (i)
resul = total / t 	
print(round(resul,2))