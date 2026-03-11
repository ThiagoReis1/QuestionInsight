from numpy import *
lista = str(input())
lista = lista.split(',')
produtos = ones(4, dtype=int)
e = 0
v = 0
a = 0
d = 0
for i in range(len(lista)):
	if lista[i].upper() == 'E':
		e+=1
	elif lista[i].upper() == 'V':
		v+=1
	elif lista[i].upper() == 'A':
		a+=1
	elif lista[i].upper() == 'D':
		d+=1

produtos[0] = e
produtos[1] = v
produtos[2] = a
produtos[3] = d
print(produtos)