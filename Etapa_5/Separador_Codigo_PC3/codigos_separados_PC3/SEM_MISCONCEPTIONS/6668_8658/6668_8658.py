from numpy import *
preco = eval(input("material: "))
soma = 0
qnt = 0

for precos in preco:
	if preco > 170.0:
		soma += preco
		qnt +=1
if qnt > 0:
	media = round(soma/qnt, 2)
else: 
	media = 0.0
print(media)
		