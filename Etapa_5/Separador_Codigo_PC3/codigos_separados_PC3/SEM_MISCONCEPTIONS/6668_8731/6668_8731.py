from numpy import *
precos = eval(input("Insira o preco do material: "))

soma = 0
contador = 0

for preco in precos:
	if preco > 170:
		soma += preco
		contador += 1
if contador > 0:
	media = round(soma / contador,2)
	print(media)
else:
	print(0.0)