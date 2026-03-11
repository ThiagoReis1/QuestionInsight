from numpy import *

notas = array(eval(input()))

i = 0
l = 0
med = 0
cont = 0
while i < size(notas):
	l += 1
	cont += l
	med += notas[i] * l
	i += 1
	
med = med / cont
print(round(med,2))