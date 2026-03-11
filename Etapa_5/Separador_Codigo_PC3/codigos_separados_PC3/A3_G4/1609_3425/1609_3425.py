from numpy import *
a = array(eval(input("")))
b = input("")

i = 0 
indice = -1

while i < size(a):
	a[i] = a[i].replace('L','R')
	if a[i] == b:
 		indice = i
	i = i + 1 

if indice >= 0:
	print(indice)
else:
	print("NAO ENCONTRADA")