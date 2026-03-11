from numpy import *

filmes = array(eval(input("preco dos filme: ")))

soma = 0
contador = 0

for preco in filmes:
	if preco > 15:
		soma += preco
		contador +=1
if contador > 0:
	media = round(soma/contador,2)
	print(media)
else:
	print(0.0)