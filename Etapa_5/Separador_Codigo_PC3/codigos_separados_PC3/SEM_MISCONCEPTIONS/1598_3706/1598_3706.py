from numpy import *

custo = array(eval(input("")))
i=0
contador=0
desconto= 0
while( contador < size(custo)):
	if (custo[i] >= 80):
		desconto = desconto + 5
		i = i + 1
		contador = contador + 1

	i = i + 1
	contador = contador + 1
resultado = sum(custo) - desconto
print(round(resultado,2))