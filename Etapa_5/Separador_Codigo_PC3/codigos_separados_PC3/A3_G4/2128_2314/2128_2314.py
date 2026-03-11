from numpy import *

aux = array(eval(input()))
m = max(aux)

aux2 = arange(3)

i = 0
j = 0
soma = 0

while i < size(aux):
	if aux[i] != m:
		soma = soma + aux[i]
	i = i + 1

media = soma/3.0

if (media >= 50.0):
	print(round(media,2))
	print("APROVADO")
else:
	print(round(media,2))
	print("REPROVADO")