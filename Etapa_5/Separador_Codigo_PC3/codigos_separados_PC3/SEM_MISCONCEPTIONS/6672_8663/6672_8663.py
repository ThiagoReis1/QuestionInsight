from numpy import *
preco = array(eval(input()))
c = 0.0
soma = 0.0

for i in range(size(preco)):
	if preco[i] > 180:
		soma += preco[i]
		c += 1
if c > 0:
	media = soma/c
	print(round(media, 2))
else:
	print(c)