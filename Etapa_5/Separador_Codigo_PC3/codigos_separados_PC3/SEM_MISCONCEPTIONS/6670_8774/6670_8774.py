from numpy import * 
vet= array(eval(input()), dtype= float)

soma = 0
contador = 0

for preco in vet:
	if preco > 20:
		soma += preco 
		contador += 1
if contador > 0:
	media= round(soma/ contador, 2)
	print(media)
else:
	print(0.0)
		

