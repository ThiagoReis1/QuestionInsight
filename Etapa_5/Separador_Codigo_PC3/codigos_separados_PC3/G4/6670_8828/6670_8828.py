from numpy import *

preco = array(eval(input("precos: ")))
i = 0
soma = 0
q = 0

while i < size(preco):
	if (preco[i]) > 20:
		soma = soma+ preco[i]
		q+=1
	i+=1

if q == 0:
	print(0.0)
else:
	print(round(soma/q, 2))