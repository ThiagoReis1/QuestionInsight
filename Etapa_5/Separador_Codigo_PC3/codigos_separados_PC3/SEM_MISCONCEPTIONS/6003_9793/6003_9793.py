cenouras = int(input('Quantas cenouras: '))

if cenouras < 5:
	valor = cenouras * 1.2
else:
	valor = cenouras * 0.9

print(round(valor,2))