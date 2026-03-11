from numpy import *
notas = array(eval(input()))
peso = [2,1,5]

i = 0
num = 0
den = 0

while i < size(notas):
	num += (notas[i] * peso[i])
	den += peso[i]
	i += 1

coef = (num/den)
print(round(coef,2))