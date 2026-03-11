from numpy import *

preco = eval(input(''))
soma  = 0
contador = 0

for me in preco:
	if me > 170 :
		soma += me
		contador += 1
if contador > 0:
	media = round(soma/contador,2)
	print(media)
else:
	print(0.0)