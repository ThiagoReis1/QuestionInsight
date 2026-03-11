from numpy import *
lista = input().upper().split(',')
var = zeros(4, dtype=int)

for i in range(size(lista)):
	if lista[i] == 'A':
		var[0] += 1
	elif lista[i] == 'P':
		var[1] += 1
	elif lista[i] == 'D':
		var[2] += 1
	elif lista[i] == 'M':
		var[3] += 1
print(var)

