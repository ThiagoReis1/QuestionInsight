from numpy import *
notas = array(eval(input("notas")))
pesos = [1,3,2,5]

i=0
somanotas =0
somapesos=0
while i < size(notas):
	somanotas = somanotas + notas[i]*pesos[i]
	somapesos = somapesos + pesos[i]
	i=i+1

total = somanotas/somapesos

total = round(total, 2)
print(total)