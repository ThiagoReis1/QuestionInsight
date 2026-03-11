from numpy import*
precos = eval(input("insira o preco do filme: "))

soma = 0
contador = 0

for preco in precos:
	if preco > 15:
		soma += preco
		contador += 1
if contador > 0:
	media = round(soma/contador, 2)
	print(media)
else:
	print(0.0)