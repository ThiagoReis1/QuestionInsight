from numpy import *

vet = array(eval(input("Digite os precos: ")))

soma = 0
contador = 0

for i in vet:
	if i > 15:
		soma = soma + i
		contador = contador + 1
if contador > 0:
	media = soma / contador
	print(round(media, 2))
else:
	print(0.0)